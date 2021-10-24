/**
 * jQuery Formset 1.5-pre
 * @author Stanislaus Madueke (stan DOT madueke AT gmail DOT com)
 * @requires jQuery 1.2.6 or later
 *
 * Copyright (c) 2009, Stanislaus Madueke
 * All rights reserved.
 *
 * Licensed under the New BSD License
 * See: http://www.opensource.org/licenses/bsd-license.php
 */
// var $ = django.jQuery;
 ;(function($) {
    $.fn.formset = function(opts)
    {
        var options = $.extend({}, $.fn.formset.defaults, opts),
            flatExtraClasses = options.extraClasses.join(' '),
            totalForms = document.querySelector('#id_' + options.prefix + '-TOTAL_FORMS'),
            maxForms = document.querySelector('#id_' + options.prefix + '-MAX_NUM_FORMS'),
            minForms = document.querySelector('#id_' + options.prefix + '-MIN_NUM_FORMS'),
            childElementSelector = 'input,select,textarea,label,div',
            $$ = document.querySelector(this),

            applyExtraClasses = function(row, ndx) {
                if (options.extraClasses) {
                    row.removeClass(flatExtraClasses);
                    row.classList.add(options.extraClasses[ndx % options.extraClasses.length]);
                }
            },

            updateElementIndex = function(elem, prefix, ndx) {
                var idRegex = new RegExp(prefix + '-(\d+|__prefix__)-'),
                    replacement = prefix + '-' + ndx + '-';
                if (elem.attr("for")) elem.attr("for", elem.attr("for").replace(idRegex, replacement));
                if (elem.attr('id')) elem.attr('id', elem.attr('id').replace(idRegex, replacement));
                if (elem.attr('name')) elem.attr('name', elem.attr('name').replace(idRegex, replacement));
            },

            hasChildElements = function(row) {
                return row.querySelector(childElementSelector).length > 0;
            },

            showAddButton = function() {
                return maxForms.length == 0 ||   // For Django versions pre 1.2
                    (maxForms.value == '' || (maxForms.value - totalForms.value > 0));
            },

            /**
            * Indicates whether delete link(s) can be displayed - when total forms > min forms
            */
            showDeleteLinks = function() {
                return minForms.length == 0 ||   // For Django versions pre 1.7
                    (minForms.value == '' || (totalForms.value - minForms.value > 0));
            },

            insertDeleteLink = function(row) {
                var delCssSelector = $.trim(options.deleteCssClass).replace(/s+/g, '.'),
                    addCssSelector = $.trim(options.addCssClass).replace(/s+/g, '.');

                var delButtonHTML = '<a class="' + options.deleteCssClass + '" href="javascript:void(0)">' + options.deleteText +'</a>';
                if (options.deleteContainerClass) {
                    // If we have a specific container for the remove button,
                    // place it as the last child of that container:
                    row.querySelector('[class*="' + options.deleteContainerClass + '"]').insertAdjacentHTML("beforeend",delButtonHTML);
                } else if (row.is('TR')) {
                    // If the forms are laid out in table rows, insert
                    // the remove button into the last table cell:
                    row.children(':last').insertAdjacentHTML("beforeend",delButtonHTML);
                } else if (row.is('UL') || row.is('OL')) {
                    // If they're laid out as an ordered/unordered list,
                    // insert an <li> after the last list item:
                    row.insertAdjacentHTML("beforeend",'<li>' + delButtonHTML + '</li>');
                } else {
                    // Otherwise, just insert the remove button as the
                    // last child element of the form's container:
                    row.insertAdjacentHTML("beforeend",delButtonHTML);
                }

                // Check if we're under the minimum number of forms - not to display delete link at rendering
                if (!showDeleteLinks()){
                    row.querySelector('a.' + delCssSelector).hide();
                }

                row.querySelector('a.' + delCssSelector).click(function() {
                    var row = document.querySelector(this).parents('.' + options.formCssClass),
                        del = row.querySelector('input:hidden[id $= "-DELETE"]'),
                        buttonRow = row.siblings("a." + addCssSelector + ', .' + options.formCssClass + '-add'),
                        forms;
                    console.log(del);
                    if (del.length) {
                        // We're dealing with an inline formset.
                        // Rather than remove this form from the DOM, we'll mark it as deleted
                        // and hide it, then let Django handle the deleting:
                        del.val('on');
                        row.hide();
                        forms = document.querySelector('.' + options.formCssClass).not(':hidden');
                        totalForms.val(forms.length);
                    } else {
                        row.remove();
                        // Update the TOTAL_FORMS count:
                        forms = document.querySelector('.' + options.formCssClass).not('.formset-custom-template');
                        totalForms.val(forms.length);
                    }
                    for (var i=0, formCount=forms.length; i<formCount; i++) {
                        // Apply `extraClasses` to form rows so they're nicely alternating:
                        applyExtraClasses(forms.eq(i), i);
                        if (!del.length) {
                            // Also update names and IDs for all child controls (if this isn't
                            // a delete-able inline formset) so they remain in sequence:
                            forms.eq(i).querySelector(childElementSelector).each(function() {
                                updateElementIndex(document.querySelector(this), options.prefix, i);
                            });
                        }
                    }
                    // Check if we've reached the minimum number of forms - hide all delete link(s)
                    if (!showDeleteLinks()){
                        document.querySelector('a.' + delCssSelector).each(function(){document.querySelector(this).hide();});
                    }
                    // Check if we need to show the add button:
                    if (buttonRow.is(':hidden') && showAddButton()) buttonRow.show();
                    // If a post-delete callback was provided, call it with the deleted form:
                    if (options.removed) options.removed(row);
                    return false;
                });
            };

        $$.each(function(i) {
            var row = document.querySelector(this),
                del = row.querySelector('input:checkbox[id $= "-DELETE"]');
            if (del.length) {
                // If you specify "can_delete = True" when creating an inline formset,
                // Django adds a checkbox to each form in the formset.
                // Replace the default checkbox with a hidden field:
                if (del.is(':checked')) {
                    // If an inline formset containing deleted forms fails validation, make sure
                    // we keep the forms hidden (thanks for the bug report and suggested fix Mike)
                    del.before('<input type="hidden" name="' + del.attr('name') +'" id="' + del.attr('id') +'" value="on" />');
                    row.hide();
                } else {
                    del.before('<input type="hidden" name="' + del.attr('name') +'" id="' + del.attr('id') +'" />');
                }
                // Hide any labels associated with the DELETE checkbox:
                document.querySelector('label[for="' + del.attr('id') + '"]').hide();
                del.remove();
            }
            if (hasChildElements(row)) {
                row.classList.add(options.formCssClass);
                if (row.is(':visible')) {
                    insertDeleteLink(row);
                    applyExtraClasses(row, i);
                }
            }
        });

        if ($$.length) {
            var hideAddButton = !showAddButton(),
                addButton, template;
            if (options.formTemplate) {
                // If a form template was specified, we'll clone it to generate new form instances:
                template = (options.formTemplate instanceof $) ? options.formTemplate : document.querySelector(options.formTemplate);
                template.removeAttr('id').classList.add(options.formCssClass + ' formset-custom-template');
                template.querySelector(childElementSelector).each(function() {
                    updateElementIndex(document.querySelector(this), options.prefix, '__prefix__');
                });
                insertDeleteLink(template);
            } else {
                // Otherwise, use the last form in the formset; this works much better if you've got
                // extra (>= 1) forms (thnaks to justhamade for pointing this out):
                if (options.hideLastAddForm) document.querySelector('.' + options.formCssClass + ':last').hide();
                template = document.querySelector('.' + options.formCssClass + ':last').clone(true).removeAttr('id');
                template.querySelector('input:hidden[id $= "-DELETE"]').remove();
                // Clear all cloned fields, except those the user wants to keep (thanks to brunogola for the suggestion):
                template.querySelector(childElementSelector).not(options.keepFieldValues).each(function() {
                    var elem = document.querySelector(this);
                    // If this is a checkbox or radiobutton, uncheck it.
                    // This fixes Issue 1, reported by Wilson.Andrew.J:
                    if (elem.is('input:checkbox') || elem.is('input:radio')) {
                        elem.attr('checked', false);
                    } else {
                        elem.val('');
                    }
                });
            }
            // FIXME: Perhaps using $.data would be a better idea?
            options.formTemplate = template;

            var addButtonHTML = '<a class="' + options.addCssClass + '" href="javascript:void(0)">' + options.addText + '</a>';
            if (options.addContainerClass) {
                // If we have a specific container for the "add" button,
                // place it as the last child of that container:
                var addContainer = document.querySelector('[class*="' + options.addContainerClass + '"');
                addContainer.insertAdjacentHTML("beforeend",addButtonHTML);
                addButton = addContainer.querySelector('[class="' + options.addCssClass + '"]');
            } else if ($$.is('TR')) {
                // If forms are laid out as table rows, insert the
                // "add" button in a new table row:
                var numCols = $$.eq(0).children().length,   // This is a bit of an assumption :|
                    buttonRow = document.querySelector('<tr><td colspan="' + numCols + '">' + addButtonHTML + '</tr>').classList.add(options.formCssClass + '-add');
                $$.parent().insertAdjacentHTML("beforeend",buttonRow);
                addButton = buttonRow.querySelector('a');
            } else {
                // Otherwise, insert it immediately after the last form:
                $$.filter(':last').after(addButtonHTML);
                addButton = $$.filter(':last').nextElementSibling;
            }

            if (hideAddButton) addButton.hide();

            addButton.click(function() {
                var formCount = parseInt(totalForms.value),
                    row = options.formTemplate.clone(true).removeClass('formset-custom-template'),
                    buttonRow = document.querySelector(document.querySelector(this).parents('tr.' + options.formCssClass + '-add').get(0) || this),
                    delCssSelector = $.trim(options.deleteCssClass).replace(/s+/g, '.');
                applyExtraClasses(row, formCount);
                row.insertBefore(buttonRow).show();
                row.querySelector(childElementSelector).each(function() {
                    updateElementIndex(document.querySelector(this), options.prefix, formCount);
                });
                totalForms.val(formCount + 1);
                // Check if we're above the minimum allowed number of forms -> show all delete link(s)
                if (showDeleteLinks()){
                    document.querySelector('a.' + delCssSelector).each(function(){document.querySelector(this).show();});
                }
                // Check if we've exceeded the maximum allowed number of forms:
                if (!showAddButton()) buttonRow.hide();
                // If a post-add callback was supplied, call it with the added form:
                if (options.added) options.added(row);
                return false;
            });
        }

        return $$;
    };

    /* Setup plugin defaults */
    $.fn.formset.defaults = {
        prefix: 'form',                  // The form prefix for your django formset
        formTemplate: null,              // The jQuery selection cloned to generate new form instances
        addText: 'Add Operator',          // Text for the add link
        deleteText: 'Remove',            // Text for the delete link
        addContainerClass: null,         // Container CSS class for the add link
        deleteContainerClass: null,      // Container CSS class for the delete link
        addCssClass: 'add-row bg-indigo-600 rounded px-4 py-2 mt-5 text-white',          // CSS class applied to the add link
        deleteCssClass: 'delete-row bg-red-600 rounded px-4 py-2 mt-10 text-white',    // CSS class applied to the delete link
        formCssClass: 'dynamic-form',    // CSS class applied to each form in a formset
        extraClasses: [],                // Additional CSS classes, which will be applied to each form in turn
        keepFieldValues: '',             // jQuery selector for fields whose values should be kept when the form is cloned
        added: null,                     // Function called each time a new form is added
        removed: null,                   // Function called each time a form is deleted
        hideLastAddForm: false           // When set to true, hide last empty add form (becomes visible when clicking on add button)
    };
})(jQuery);
