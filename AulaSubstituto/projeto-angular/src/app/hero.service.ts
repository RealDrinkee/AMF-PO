import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class HeroService {
  private heroes = [
    "Dr Nice",
    "Narco",
    "Bombasto",
    "Celeritas",
    "Magneta",
    "RubberMan",
    "Dynama",
    "Dr IQ",
    "Magma",
    "Tornado"
    ]as const;

  private heroSuperPowers: Record<typeof HeroService.prototype.heroes[number], string> = {
    DrNice: "Usar Trovao",
    Narco: "Usar Trovao",
  }
  getHeroes() {
    return this.heroes
  }

  getHeroSuportPower(hero: typeof HeroService.prototype.heroes[number]) {
    return this.heroSuperPowers[hero];
  }
  constructor() {
  }
}
