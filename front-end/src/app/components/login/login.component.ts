import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';


@Component({
  selector: 'app-login',
  standalone: false,
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})
export class LoginComponent{
  
  loginForm: FormGroup;

  constructor(private fb: FormBuilder) {
    this.loginForm = this.fb.group(
      {
        email: ['', [Validators.required, Validators.email]], // Validación de email
        password: ['', [Validators.required, Validators.minLength(6)]], // Validación de contraseña
      },
      { updateOn: 'blur' } //que se valide luego de que el usuario deja el campo 
    );
    // Retrasar la actualización del estado hasta que el usuario interactúe
    setTimeout(() => {
      this.loginForm.markAsPristine();
  });
  }
  
 
  showPassword: boolean = false;

  togglePassword() {
    this.showPassword = !this.showPassword;
  }

  onSubmit() {
    if (this.loginForm.valid) {
      console.log('Usuario:', this.loginForm.value.email);
      console.log('Contraseña:', this.loginForm.value.password);
    } else {
      console.log('El formulario no es válido.');
    }
  }
}
