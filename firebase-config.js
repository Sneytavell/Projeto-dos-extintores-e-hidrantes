// Configuração do banco (Firebase) usado no site publicado (Vercel).
// 1) Crie um projeto em https://console.firebase.google.com
// 2) Adicione um "App da Web" e copie o objeto firebaseConfig para cá.
// 3) Ative Authentication > Método de login > Anônimo, e crie o Firestore Database.
// Enquanto estiver null, o site abre sem banco (os dados ficam só no navegador).
window.FIREBASE_CONFIG = null;
/* Exemplo:
window.FIREBASE_CONFIG = {
  apiKey: "...",
  authDomain: "seu-projeto.firebaseapp.com",
  projectId: "seu-projeto",
  storageBucket: "seu-projeto.appspot.com",
  messagingSenderId: "...",
  appId: "..."
};
*/
