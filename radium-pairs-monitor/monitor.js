const axios = require('axios');
const { Connection } = require('@solana/web3.js');

// Set up your Solana connection
const SOLANA_RPC_URL = 'https://api.mainnet-beta.solana.com'; // Mainnet RPC URL
const connection = new Connection(SOLANA_RPC_URL, 'confirmed');

// Radium API endpoint for fetching trading pairs
const RADIUM_API_URL = 'https://api.raydium.io/pairs';

let lastPairs = [];

// Function to fetch current pairs from Radium
async function fetchPairs() {
    try {
        const response = await axios.get(RADIUM_API_URL);
        return response.data; // Assuming the response contains an array of pairs
    } catch (error) {
        console.error('Error fetching pairs:', error);
        return [];
    }
}

// Function to monitor new pairs
async function monitorNewPairs() {
    console.log('Monitoring new pairs on Radium V3...');
    
    while (true) {
        const currentPairs = await fetchPairs();

        // Check if the response is valid
        if (!Array.isArray(currentPairs)) {
            console.error('Unexpected response format:', currentPairs);
            await new Promise(resolve => setTimeout(resolve, 30000)); // Wait before retrying
            continue;
        }

        // Check for new pairs
        const newPairs = currentPairs.filter(pair => 
            !lastPairs.some(lastPair => lastPair.id === pair.id) // Assuming each pair has a unique 'id'
        );

        if (newPairs.length > 0) {
            console.log(`New pairs detected:`);
            newPairs.forEach(pair => {
                console.log(`- ${pair.id}: ${pair.tokenA} / ${pair.tokenB}`);
            });
        } else {
            console.log('No new pairs found.');
        }

        // Update last pairs
        lastPairs = currentPairs;

        // Wait for a specified interval before checking again
        await new Promise(resolve => setTimeout(resolve, 30000)); // Check every 30 seconds
    }
}

// Start monitoring
monitorNewPairs().catch(console.error);