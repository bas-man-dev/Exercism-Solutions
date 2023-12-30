export function hey(message: string): string {
  const whenShouting = "Whoa, chill out!";
  const genericAnswer = "Whatever.";
  const normalQuestion = "Sure.";
  const forcefulQuestion = "Calm down, I know what I'm doing!";
  const silence = "Fine. Be that way!"
  const alphabet = /[a-zA-Z]/g;
  const alphanumeric = /[a-zA-Z0-9]/g

  message = message.trim()
  if (message.endsWith("?")) {
    if (message.toUpperCase() == message && alphabet.test(message)) {
      return forcefulQuestion;
    }
    return normalQuestion;
  }
  if (message.toUpperCase() == message) {
    // Check there are letters in response
    if (alphabet.test(message)) {
      return whenShouting;
    }
  }
if (!alphanumeric.test(message)) {
  return silence
}
  return genericAnswer;
}
