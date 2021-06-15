/*odoo.define('geneos_assignment.widget_date', (require) => {
    
    const core = require('web.core');
    var registry = require('web.field_registry');
    var basic_fields = require('web.basic_fields');
    var FieldDate = basic_fields.FieldDate;
    var Widget = require('web.AbstractField');
    
    const DateField = Widget.extend({
         template: 'month_year_widget',
         xmlDependencies: ['/geneos_assignment/static/src/xml/widget_date_template.xml'],
        renderElement() { 
            console.log(this);
            if (this.value) {
                const month = this.value._d.getUTCMonth()+1;
                const year = this.value._d.getUTCFullYear();
                this.stringValue = month + "/" + year;
            }
            this._super.apply(this, arguments);

        }
    });
    console.log("eeeee");
        registry.add('month_year_widget', DateField);  

});*/