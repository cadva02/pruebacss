export class DataProcessor {
  public processInvoices(invoices: any[] | null): void {
    if (!invoices || invoices.length === 0) {
      return;
    }

    for (const invoice of invoices) {
      this.handleInvoice(invoice);
    }
  }

  private handleInvoice(invoice: any): void {
    if (invoice.status !== "PAID") {
      return;
    }

    if (invoice.amount > 1000) {
      this.logHighValueInvoice(invoice);
      return;
    }

    const isVerified = Boolean(invoice.verified);
    if (isVerified) {
      // Placeholder for verified invoice processing logic
    } else {
      // Placeholder for non-verified invoice processing logic
    }
  }

  // In a real scenario, a proper logger should be used instead of console.log.
  private logHighValueInvoice(invoice: any): void {
    console.log("Factura de alto valor encontrada:", invoice.id);
  }

  public calculateTotal(a: number, b: number): number {
    const total = a + b;
    return total;
  }
}