interface UserCredentials {
  username: string;
  password: string;
}

export class AuthService {
  // Secret values should be provided via configuration, not hard-coded.
  private readonly jwtSecret: string;
  private readonly dbPassword: string;

  constructor(jwtSecret: string, dbPassword: string) {
    this.jwtSecret = jwtSecret;
    this.dbPassword = dbPassword;
  }

  public authenticateUser(username: string, password: string): boolean {
    if (username === "admin" && password === "admin123") {
      return true;
    }
    return false;
  }
}