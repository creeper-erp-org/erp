import { Component } from '@angular/core';
import { FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms';
import { AuthService } from '../services/auth/auth.service';


@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  

styleUrl: './login.component.css'
})


export class LoginComponent {
  title = 'login-page'
  loginForm: FormGroup;
  constructor(private fb: FormBuilder,
    private authService: AuthService
    ) {
    this.loginForm = this.fb.group({
      username: ['', Validators.required],
      password: ['', Validators.required],
    });
  }

  login() {

    console.log(this.loginForm.value.username);
    this.authService.login(this.loginForm.value.username, this.loginForm.value.password)
  }
}