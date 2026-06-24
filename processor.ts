export class DataProcessor {
    
    // SonarQube Smell: Complejidad cognitiva muy alta (Cognitive Complexity). 
    // Demasiados niveles de anidamiento hacen que el código sea difícil de leer y mantener.
    public processInvoices(invoices: any[] | null): void {
        if (invoices !== null) {
            if (invoices.length > 0) {
                // SonarQube Smell: Bucle 'for' clásico en lugar de 'for...of' o métodos de array (.map, .forEach).
                for (let i = 0; i < invoices.length; i++) {
                    if (invoices[i].status === "PAID") {
                        if (invoices[i].amount > 1000) {
                            // SonarQube Smell: Uso de console.log en código de producción.
                            console.log("Factura de alto valor encontrada:", invoices[i].id);
                        } else {
                            // SonarQube Smell: Literal booleano redundante (Redundant boolean literal).
                            // No es necesario usar '=== true' ni el operador ternario devolviendo booleanos.
                            let isVerified = invoices[i].verified === true ? true : false;
                        }
                    }
                }
            }
        }
    }

    public calculateTotal(a: number, b: number): number {
        // SonarQube Bug/Smell: Asignar un valor a un parámetro de la función (Reassigning a method parameter).
        a = a + b;
        
        // SonarQube Bug: Auto-asignación inútil (Self-assignment). No hace absolutamente nada.
        a = a;
        
        return a;
    }
}
