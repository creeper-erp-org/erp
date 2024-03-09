import { Component } from '@angular/core';
import { FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  

styleUrl: './login.component.css'
})


export class LoginComponent {
  title = 'login-page'
  loginForm: FormGroup;

  constructor(private fb: FormBuilder) {
    this.loginForm = this.fb.group({
      username_val: ['', Validators.required],
      password_val: ['', Validators.required],
    });
  }

  updateUserProfile() {
    console.log(this.loginForm.value);
    
  }
}