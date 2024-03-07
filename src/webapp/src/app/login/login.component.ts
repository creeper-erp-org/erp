import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [],
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})


export class LoginComponent {
  title = 'login-page'

  // loginForm: any;
  username: string = '';
  password: string = '';
  
  updateUserProfile() {
    console.log('Hello');
    
  }
}
