EditBadge = class EditBadge {
    constructor() {
        this.bootbox = null;
    }

    openDialog() {
        this.bootbox = bootbox.dialog({
            className: 'editBadge',
            message: 'editBadge',
            onEscape: true
        }).init(() => {
            const bodySelector = $('.editBadge .bootbox-body');
            bodySelector.html('');
            Blaze.render(Template.editBadge, bodySelector.get(0));
            $('.panel-collapse').hide();
            $('.panel-sidebar').hide();
        });

        this.bootbox.on('shown.bs.modal', function() {
            $('.close').focus();
        });
    }

    closeBootbox() {
        bootbox.hideAll();
    }
};
