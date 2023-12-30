export function isPangram(letters: string) {
  let newLetters = letters.toLowerCase();
  let alphabet: string = "abcdefghijklmnopqrstuvwxyz";

  [...newLetters].forEach((item: string) => {
    if (alphabet.includes(item)) {
      alphabet = alphabet.replace(item, "");
    }
  });

  return alphabet.length == 0 ? true : false;
}
