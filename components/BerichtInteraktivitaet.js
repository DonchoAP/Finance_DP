import { useState, useEffect } from 'react';
import { Chart } from 'react-chartjs-2';
import { Chart as ChartJS, CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend } from 'chart.js';
import BerichtInteraktivitaet from '../components/BerichtInteraktivitaet';

export default function BerichteSeite() {
  const anfangsDaten = {
    labels: ['Januar', 'Februar', 'März', 'April', 'Mai', 'Juni'],
    datasets: [{
      label: 'Verkäufe',
      data: [12, 19, 3, 5, 2, 3],
      backgroundColor: 'rgba(75, 192, 192, 0.6)',
    }]
  };

  return (
    <div>
      <h1>Berichteseite</h1>
      <BerichtInteraktivitaet anfangsDaten={anfangsDaten} />
    </div>
  );
}