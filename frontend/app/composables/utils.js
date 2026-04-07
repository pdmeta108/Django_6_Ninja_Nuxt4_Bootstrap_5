// Exportamos funciones individuales
export const utils = () => {

  // Tu función de sumar
  const sumar = (a, b) => {
    return a + b
  }

  // Tu función de restar
  const restar = (x, y) => {
    return x - y
  }

  return {
    sumar,
    restar
  }
}