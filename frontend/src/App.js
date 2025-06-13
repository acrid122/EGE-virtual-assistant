import React from 'react';
import { init } from '@telegram-apps/sdk';

const telegram = init();

function App() {
  console.log(telegram.initDataUnsafe.user); // Данные пользователя Telegram
  return (
    <div>
      <h1>EGE Virtual Assistant</h1>
      <p>Welcome to the Telegram Web App!</p>
    </div>
  );
}

export default App;