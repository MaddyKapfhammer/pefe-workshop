# This is a file to be used for prompt engineering challenge 3

class InvoiceProcessor:
    def __init__(self, db_conn):
        self.db = db_conn

    def generate_invoice(self, user_id, items):
        total = sum(item['price'] * item['quantity'] for item in items)
        invoice_id = self.db.insert_invoice(user_id, total)
        for item in items:
            self.db.insert_line_item(invoice_id, item['name'], item['price'], item['quantity'])
        self.db.log_invoice_creation(invoice_id)
        return invoice_id

    def refund_invoice(self, invoice_id):
        line_items = self.db.get_line_items(invoice_id)
        for item in line_items:
            self.db.process_refund(item['name'], item['price'], item['quantity'])
        self.db.mark_invoice_refunded(invoice_id)

    def summarize_invoice(self, invoice_id):
        items = self.db.get_line_items(invoice_id)
        summary = {item['name']: item['quantity'] for item in items}
        return summary

