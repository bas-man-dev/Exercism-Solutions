const fourRolls = () => {
  let score = 0;
  let scores: number[] = [];

  for (let i = 0; i < 4; i++) {
    score = Math.floor(Math.random() * 6) + 1;
    scores.push(score);
  }
  return scores;
};

const getStat = () => {
  const initialThrows: number[] = fourRolls();
  let stat = 0;
  // Get the top 3 throws
  initialThrows.sort((a, b) => a - b).shift();
  // Add the throws
  initialThrows.forEach((item) => (stat += item));
  return stat;
};
export class DnDCharacter {
  strength?: number;
  dexterity?: number;
  constitution?: number;
  intelligence?: number;
  wisdom?: number;
  charisma?: number;
  hitpoints?: number;

  public constructor() {
    this.strength = getStat();
    this.dexterity = getStat();
    this.constitution = getStat();
    this.intelligence = getStat();
    this.wisdom = getStat();
    this.charisma = getStat();
    this.hitpoints = Math.floor((this.constitution - 10) / 2) + 10
  }

  public static generateAbilityScore(): number {
    return getStat();
  } // do I need this??

  public static getModifierFor(abilityValue: number): number {
    return Math.floor((abilityValue - 10) / 2);
  }
}
