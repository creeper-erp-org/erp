import { Component } from '@angular/core';
import { FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms';
import { AuthService } from '../services/auth/auth.service';
import { Observable, catchError, of, throwError } from 'rxjs';


@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  

styleUrl: './login.component.css'
})


export class LoginComponent {
  title = 'login-page'
  loginForm: FormGroup;
  data: any;
  errMes: string | null = null
  constructor(private fb: FormBuilder,
    private authService: AuthService
    ) {
    this.loginForm = this.fb.group({
      username: ['', Validators.required],
      password: ['', Validators.required],
    });
  }

  login() {
    
    this.authService.login(this.loginForm.value.username, this.loginForm.value.password).subscribe(response => {
      this.data = response;
      console.log(this.data);
    }, error => {
      let err = error.error
      this.errMes = err.error
    }
    );
  }
}