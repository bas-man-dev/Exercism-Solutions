import { score } from './darts'
import { expect, test, describe } from "bun:test";

describe('Darts', () => {
  test('Missed target', () => {
    expect(score(-9, 9)).toEqual(0)
  })

  test('On the outer circle', () => {
    expect(score(0, 10)).toEqual(1)
  })

  test('On the middle circle', () => {
    expect(score(-5, 0)).toEqual(5)
  })

  test('On the inner circle', () => {
    expect(score(0, -1)).toEqual(10)
  })

  test('Exactly on centre', () => {
    expect(score(0, 0)).toEqual(10)
  })

  test('Near the centre', () => {
    expect(score(-0.1, -0.1)).toEqual(10)
  })

  test('Just wtesthin the inner circle', () => {
    expect(score(0.7, 0.7)).toEqual(10)
  })

  test('Just outside the inner circle', () => {
    expect(score(0.8, -0.8)).toEqual(5)
  })

  test('Just wtesthin the middle circle', () => {
    expect(score(-3.5, 3.5)).toEqual(5)
  })

  test('Just outside the middle circle', () => {
    expect(score(-3.6, -3.6)).toEqual(1)
  })

  test('Just wtesthin the outer circle', () => {
    expect(score(-7.0, 7.0)).toEqual(1)
  })

  test('Just outside the outer circle', () => {
    expect(score(7.1, -7.1)).toEqual(0)
  })

  test('Asymmetric postestion between the inner and middle circles', () => {
    expect(score(0.5, -4)).toEqual(5)
  })
})
