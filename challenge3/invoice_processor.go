package invoice

import "fmt"

type DB interface {
	InsertInvoice(userID string, total float64) string
	InsertLineItem(invoiceID, name string, price float64, quantity int)
	LogInvoiceCreation(invoiceID string)
	GetLineItems(invoiceID string) []LineItem
	ProcessRefund(name string, price float64, quantity int)
	MarkInvoiceRefunded(invoiceID string)
}

type LineItem struct {
	Name     string
	Price    float64
	Quantity int
}

type InvoiceProcessor struct {
	db DB
}

func NewInvoiceProcessor(db DB) *InvoiceProcessor {
	return &InvoiceProcessor{db: db}
}

func (p *InvoiceProcessor) GenerateInvoice(userID string, items []LineItem) string {
	total := 0.0
	for _, item := range items {
		total += item.Price * float64(item.Quantity)
	}
	invoiceID := p.db.InsertInvoice(userID, total)
	for _, item := range items {
		p.db.InsertLineItem(invoiceID, item.Name, item.Price, item.Quantity)
	}
	p.db.LogInvoiceCreation(invoiceID)
	return invoiceID
}

func (p *InvoiceProcessor) RefundInvoice(invoiceID string) {
	items := p.db.GetLineItems(invoiceID)
	for _, item := range items {
		p.db.ProcessRefund(item.Name, item.Price, item.Quantity)
	}
	p.db.MarkInvoiceRefunded(invoiceID)
}

func (p *InvoiceProcessor) SummarizeInvoice(invoiceID string) map[string]int {
	items := p.db.GetLineItems(invoiceID)
	summary := make(map[string]int)
	for _, item := range items {
		summary[item.Name] += item.Quantity
	}
	return summary
}
