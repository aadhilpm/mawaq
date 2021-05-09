# -*- coding: utf-8 -*-
# Copyright (c) 2020, Aadhil and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe import _, msgprint

class Members(Document):
    pass
"""
     def validate(self):
        self.add_journal():
    
      def add_journal(self):
        try:
            if(self.docstatus == 1 and self.status == "Active"):
                doc = frappe.new_doc("Journal Entry")
                doc.voucher_type = "Journal Entry"
                doc.posting_date = frappe.utils.nowdate()

                doc.append("accounts",{
                    "account": "Members Sub Receivable - M",
                    "account_currency": "QAR",
                    "party_type": "Members",
                    "party": self.name,
                    "against_account": self.name,
                    "cost_center": "Main - M",
                    "credit_in_account_currency": self.membership_amount
                })

                doc.append("accounts",{
                    "account": "Subscription Received 2020 - M",
                    "account_currency": "QAR",
                    "party_type": "Members",
                    "party": self.name,
                    "against_account": "Members Sub Receivable - M",
                    "cost_center": "Main - M",
                    "debit_in_account_currency": self.membership_amount
                })

                doc.save()
                doc.submit()

                self.append("membership_subscription_entries", {
                    "journal_entry": doc.name,
                    "amount": doc.total_debit,
                    "date": doc.posting_date
                })
        except Exception as e:
            frappe.msgprint(e)
"""
