import { Component } from '@angular/core';

@Component({
  selector: 'app-login',
  standalone: false,
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})
export class LoginComponent {
  username: string = '';
  password: string = '';

  onSubmit() {
    // Aquí puedes añadir la lógica para manejar el inicio de sesión
    console.log('Usuario:', this.username);
    console.log('Contraseña:', this.password);
  }

}
