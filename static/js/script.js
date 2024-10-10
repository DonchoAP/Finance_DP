import { useState, useEffect } from 'react';
import { Chart } from 'react-chartjs-2';
import { Chart as ChartJS, CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend } from 'chart.js';

ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend);

const BerichtInteraktivitaet = ({ anfangsDaten }) => {
  const [daten, setDaten] = useState(anfangsDaten);
  const [ausgewaehlterFilter, setAusgewaehlterFilter] = useState('alle');

  useEffect(() => {
    // Hier könnten Sie einen API-Aufruf machen, um aktualisierte Daten zu erhalten
    // Vorerst verwenden wir die Anfangsdaten
  }, []);

  const datenFiltern = (filter) => {
    setAusgewaehlterFilter(filter);
    // Hier würden Sie die tatsächliche Filterlogik implementieren
    // Vorerst simulieren wir nur eine Änderung
    setDaten({
      ...daten,
      datasets: [{
        ...daten.datasets[0],
        data: daten.datasets[0].data.map(wert => wert * (filter === 'alle' ? 1 : 0.5))
      }]
    });
  };

  const diagrammOptionen = {
    responsive: true,
    plugins: {
      legend: {
        position: 'top',
      },
      title: {
        display: true,
        text: 'Interaktiver Bericht',
      },
    },
  };

  return (
    <div>
      <div>
        <button onClick={() => datenFiltern('alle')}>Alle</button>
        <button onClick={() => datenFiltern('letzterMonat')}>Letzter Monat</button>
        <button onClick={() => datenFiltern('letzteWoche')}>Letzte Woche</button>
      </div>
      <Chart type="bar" data={daten} options={diagrammOptionen} />
    </div>
  );
};

export default BerichtInteraktivitaet;