import {Component, EventEmitter, inject, Output} from '@angular/core';
import { HeroService} from "../hero.service";

@Component({
  selector: 'app-hero-list',
  templateUrl: './hero-list.component.html',
  styleUrls: ['./hero-list.component.sass']
})
export class HeroListComponent {
  @Output() selectHero = new EventEmitter<string>();
  heroService = inject(HeroService);

  heroes = this.heroService.getHeroes();
}
