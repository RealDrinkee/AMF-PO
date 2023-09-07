import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.sass']
})
export class AppComponent {
  selectedHero: string = '';

 selectHero(hero: string) {
   console.log(hero);
   this.selectedHero = hero;
 }
}

