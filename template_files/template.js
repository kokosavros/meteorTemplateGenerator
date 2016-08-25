{{classname}} = class {{classname}} {
    constructor() {
        this.bootbox = null;
    }

    openDialog() {
        this.bootbox = bootbox.dialog({
            className: '{{template}}',
            message: '{{template}}',
            onEscape: true
        }).init(() => {
            const bodySelector = $('.{{template}} .bootbox-body');
            bodySelector.html('');
            Blaze.render(Template.{{template}}, bodySelector.get(0));
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
