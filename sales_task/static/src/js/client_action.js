/** @odoo-module */
import { registry } from '@web/core/registry';
import { useService } from "@web/core/utils/hooks";
const { Component } = owl;

export class SuccessMessageModal extends Component {
    setup() {
        this.dialog = useService("dialog");
    }

    openModal() {
        this.dialog.add('alert', {
            title: 'Success!',
            message: 'Your action was successful.',
            confirm_text: 'OK',
            callback: () => {
                console.log('Modal closed');
            }
        });
    }
}

SuccessMessageModal.template = "client_action.success_message";
registry.category("actions").add("show_success_message", SuccessMessageModal);
