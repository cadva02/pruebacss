// SonarQube Smell: Interfaz vacía (Empty interface). No aporta ningún valor.
interface UserCredentials {}

export class AuthService {
    // SonarQube Vulnerability/Security Hotspot: Credenciales o secretos hardcodeados en el código.
    private readonly jwtSecret = "super-secret-token-123456789";
    private readonly dbPassword = "root_password!";

    // SonarQube Smell: Uso de 'any'. Derrota el propósito de TypeScript (Type safety).
    public authenticateUser(username: any, password: any): boolean {
        // SonarQube Smell: Variable declarada pero nunca utilizada (Unused local variable).
        const maxRetries = 3;

        // SonarQube Smell: Asignación inútil. El valor se sobrescribe antes de usarse.
        let isAuthenticated = false;
        
        // SonarQube Bug: Uso de '==' en lugar de '===' (Equality operators should not be used).
        // En JS/TS, '==' puede causar coerción de tipos inesperada.
        if (username == "admin" && password == "admin123") {
            isAuthenticated = true;
            return true;
        } else {
            isAuthenticated = false;
            return false;
        }

        // SonarQube Bug: Código inalcanzable (Unreachable code). El 'return' detiene la ejecución antes. pruebaaa
        console.log("Autenticación finalizada");
    }
}
