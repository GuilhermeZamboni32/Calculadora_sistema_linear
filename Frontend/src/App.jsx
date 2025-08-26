// LinearSystemCalculator.js
import React, { useState } from 'react';
import './App.css'

// Nota: A lógica de cálculo real (álgebra linear) não está implementada.
// Esta é uma simulação da interface com resultados pré-definidos.
const solveSystem = (size, equations) => {
  if (size === 2) {
    // Simula o resultado para o exemplo 2x2 da imagem
    return { X: 1, Y: 2 };
  }
  if (size === 3) {
    // Simula o resultado para o exemplo 3x3 da imagem
    return { X: 1, Y: 2, Z: 3 };
  }
  return {};
};

const App = ({ title, size, initialEquations }) => {
  const [equations, setEquations] = useState(initialEquations);
  const [result, setResult] = useState(null);

  const handleInputChange = (rowIndex, colIndex, value) => {
    // Cria uma cópia da matriz de equações para não modificar o estado diretamente
    const newEquations = equations.map((row, rIdx) => {
      if (rIdx === rowIndex) {
        return row.map((col, cIdx) => (cIdx === colIndex ? value : col));
      }
      return row;
    });
    setEquations(newEquations);
  };

  const handleCalculate = () => {
    // Aqui entraria a lógica real de cálculo.
    // Por enquanto, usamos a função de simulação.
    const solution = solveSystem(size, equations);
    setResult(solution);
  };

  const variables = ['X', 'Y', 'Z'];

  return (
    <div className="calculator-card">
      <h2>{title}</h2>
      <div className="equations-container">
        {equations.map((row, rowIndex) => (
          <div key={rowIndex} className="equation-row">
            {row.slice(0, -1).map((value, colIndex) => (
              <React.Fragment key={colIndex}>
                <input
                  type="number"
                  value={value}
                  onChange={(e) => handleInputChange(rowIndex, colIndex, e.target.value)}
                />
                <span>{variables[colIndex]}</span>
                {colIndex < size - 1 && <span>+</span>}
              </React.Fragment>
            ))}
            <span>=</span>
            <input
              type="number"
              value={row[size]}
              onChange={(e) => handleInputChange(rowIndex, size, e.target.value)}
            />
          </div>
        ))}
      </div>
      <button onClick={handleCalculate}>Calcular</button>
      
      {result && (
        <div className="result-section">
          <h3>Resultado</h3>
          <div className="result-values">
            {Object.entries(result).map(([variable, value]) => (
              <div key={variable} className="result-item">
                {variable} = {value}
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
};

export default App;