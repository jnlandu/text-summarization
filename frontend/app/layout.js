import 'bootstrap/dist/css/bootstrap.min.css'
import "./globals.css";
import { AuthProvider } from '../context/AuthContext';

export default function RootLayout({ children }) {
  return (
    <AuthProvider>
    <html lang="en">
      <body>
        {children}
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossOrigin="anonymous"></script>
       <script>
        
       </script>
      </body>
    </html>
    </AuthProvider>
  );
}
