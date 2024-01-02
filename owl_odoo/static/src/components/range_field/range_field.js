/** @odoo-module **/

import { registry } from "@web/core/registry";
import { standardFieldProps } from "@web/views/fields/standard_field_props";

import { Component, useState, onWillUpdateProps } from "@odoo/owl";

export class RangeField extends Component {
    setup() {
        this.state = useState({
            range: this.props.value || '',
        });
        const { currency_id } = this.props.record.data
        this.currency = currency_id ? currency_id[1] : ""


    }


}
//this is the template xml
RangeField.template = "owl.RangeField";
//this the standard_Field_props.js
RangeField.props = {
    ...standardFieldProps,
};

RangeField.supportedTypes = ["integer"];
//the range is widget and RangeField is the class
registry.category("fields").add("range", RangeField);
