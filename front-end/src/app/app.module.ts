import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginComponent } from './components/login/login.component';
import { ReactiveFormsModule } from '@angular/forms';
import { FormsModule } from '@angular/forms';
import { ContactenosComponent } from './components/contactenos/contactenos.component';

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    ContactenosComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    //Importar Reactive Form Module para  trabajar los fomularios
    ReactiveFormsModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
