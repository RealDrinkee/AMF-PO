import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class HeroService {
<<<<<<< HEAD

  constructor() { }
=======
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
>>>>>>> 1c5a191e1371e0da1e048d19a32b1a03bd637764
}
