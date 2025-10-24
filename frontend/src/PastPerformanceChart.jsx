
import { Line } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

const PastPerformanceChart = ({ revenueData, netIncomeData }) => {
  const data = {
    labels: Object.keys(revenueData).map(d => new Date(d).getFullYear()),
    datasets: [
      {
        label: 'Total Revenue',
        data: Object.values(revenueData),
        borderColor: 'rgb(54, 162, 235)',
        backgroundColor: 'rgba(54, 162, 235, 0.5)',
      },
      {
        label: 'Net Income',
        data: Object.values(netIncomeData),
        borderColor: 'rgb(255, 99, 132)',
        backgroundColor: 'rgba(255, 99, 132, 0.5)',
      },
    ],
  };

  const options = {
    responsive: true,
    plugins: {
      legend: {
        position: 'top',
      },
      title: {
        display: true,
        text: 'Past Performance',
      },
    },
  };

  return <Line options={options} data={data} />;
};

export default PastPerformanceChart;
