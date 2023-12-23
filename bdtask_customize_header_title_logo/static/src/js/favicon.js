/** @odoo-module **/

import { WebClient } from "@web/webclient/webclient";
import { patch } from "web.utils";

patch(WebClient.prototype, "bdtask_customize_header_title_logo.WebClient", {
    setup() {
        this._super();
        this.title.setParts({ zopenerp: "Custom" });
    },
});