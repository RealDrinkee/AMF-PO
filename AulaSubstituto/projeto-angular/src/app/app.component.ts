import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.sass']
})
export class AppComponent {
  title = 'projeto-angular';

  ClickButton() {
    this.title = 'O título foi alterado';
  }
}

