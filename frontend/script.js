
const BACKEND_API_URL = 'http://localhost:5000/api/extract-data';

async function fetchBackendData() {
    document.getElementById('loadingSpinner').style.display = 'block';
    try {
        const response = await fetch(BACKEND_API_URL);
        if (!response.ok) throw new Error('Failed to fetch data');
        const data = await response.json();
        document.getElementById('loadingSpinner').style.display = 'none';
        return data;
    } catch (error) {
        document.getElementById('loadingSpinner').style.display = 'none';
        console.error(error);
    }
}

function downloadCSV(data) {
    const csvContent = data.map(row => Object.values(row).join(',')).join('\n');
    const blob = new Blob([csvContent], { type: 'text/csv' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'data.csv';
    a.click();
}

document.getElementById('csvButton').addEventListener('click', async () => {
    const data = await fetchBackendData();
    if (data) downloadCSV(data);
});
