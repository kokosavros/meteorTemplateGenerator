{{template}} = new {{classname}}();

// Call this function to open the Modal
{{openModal}} = function() {
    {{template}} = new {{classname}}();
    {{template}}.openDialog();
};

Template.{{template}}.onRendered(function() {});

Template.{{template}}.onCreate(function() {});

Template.{{template}}.helpers({});

Template.{{template}}.events({});
