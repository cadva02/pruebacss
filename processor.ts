export class DataProcessor {
  // SonarQube Smell: Complejidad cognitiva muy alta (Cognitive Complexity).
  // Demasiados niveles de anidamiento hacen que el código sea difícil de leer y mantener.
  public processInvoices(invoices: any[] | null): void {
    if (!invoices || invoices.length === 0) {
      return;
    }

    for (const invoice of invoices) {
      if (invoice.status !== "PAID") {
        continue;
      }

      if (invoice.amount > 1000) {
        // SonarQube Smell: Uso de console.log en código de producción.
        console.log("Factura de alto valor encontrada:", invoice.id);
      } else {
        // SonarQube Smell: Literal booleano redundante (Redundant boolean literal).
        // No es necesario usar '=== true' ni el operador ternario devolviendo booleanos.
        const isVerified = !!invoice.verified;
      }
    }
  }

  public calculateTotal(a: number, b: number): number {
    return a + b;
  }
}