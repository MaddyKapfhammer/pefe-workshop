class InvoiceProcessor {
  constructor(dbConn) {
    this.db = dbConn;
  }

  generateInvoice(userId, items) {
    const total = items.reduce((sum, item) => sum + item.price * item.quantity, 0);
    const invoiceId = this.db.insertInvoice(userId, total);
    items.forEach(item => {
      this.db.insertLineItem(invoiceId, item.name, item.price, item.quantity);
    });
    this.db.logInvoiceCreation(invoiceId);
    return invoiceId;
  }

  refundInvoice(invoiceId) {
    const lineItems = this.db.getLineItems(invoiceId);
    lineItems.forEach(item => {
      this.db.processRefund(item.name, item.price, item.quantity);
    });
    this.db.markInvoiceRefunded(invoiceId);
  }

  summarizeInvoice(invoiceId) {
    const items = this.db.getLineItems(invoiceId);
    const summary = {};
    items.forEach(item => {
      summary[item.name] = item.quantity;
    });
    return summary;
  }
}
