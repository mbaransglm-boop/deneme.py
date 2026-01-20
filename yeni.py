<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Genel Yorum Duvarı</title>
    <!-- Tailwind CSS for styling -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Firebase SDKs -->
    <script type="module">
        import { initializeApp } from "https://www.gstatic.com/firebasejs/11.1.0/firebase-app.js";
        import { getFirestore, collection, addDoc, onSnapshot, query, serverTimestamp } from "https://www.gstatic.com/firebasejs/11.1.0/firebase-firestore.js";
        import { getAuth, signInAnonymously, onAuthStateChanged } from "https://www.gstatic.com/firebasejs/11.1.0/firebase-auth.js";

        // --- FIREBASE CONFIGURATION ---
        // GitHub'a yüklerken bu kısmı kendi Firebase konsolunuzdan aldığınız bilgilerle değiştirin.
        // Mevcut haliyle önizleme ortamında çalışacaktır.
        const firebaseConfig = JSON.parse(typeof __firebase_config !== 'undefined' ? __firebase_config : '{}');
        const appId = typeof __app_id !== 'undefined' ? __app_id : 'default-comment-app';

        // Initialize Firebase
        const app = initializeApp(firebaseConfig);
        const auth = getAuth(app);
        const db = getFirestore(app);

        // State Management
        let currentUser = null;
        const commentForm = document.getElementById('commentForm');
        const commentList = document.getElementById('commentList');
        const submitBtn = document.getElementById('submitBtn');
        const errorAlert = document.getElementById('errorAlert');

        // Authentication
        async function initAuth() {
            try {
                await signInAnonymously(auth);
                onAuthStateChanged(auth, (user) => {
                    currentUser = user;
                    if (user) loadComments();
                });
            } catch (error) {
                showError("Veritabanına bağlanılamadı. Lütfen Firebase ayarlarınızı kontrol edin.");
            }
        }

        // Load Comments
        function loadComments() {
            // Rule 1: Using the mandatory path structure
            const commentsRef = collection(db, 'artifacts', appId, 'public', 'data', 'comments');
            const q = query(commentsRef);

            onSnapshot(q, (snapshot) => {
                const comments = [];
                snapshot.forEach((doc) => {
                    comments.push({ id: doc.id, ...doc.data() });
                });

                // Rule 2: Sorting in memory (Newest first)
                comments.sort((a, b) => {
                    const timeA = b.createdAt?.seconds || 0;
                    const timeB = a.createdAt?.seconds || 0;
                    return timeA - timeB;
                });

                renderComments(comments);
            }, (err) => {
                showError("Yorumlar yüklenirken bir hata oluştu.");
            });
        }

        // Render UI
        function renderComments(comments) {
            if (comments.length === 0) {
                commentList.innerHTML = `
                    <div class="text-center py-10 border-2 border-dashed border-gray-200 rounded-2xl">
                        <p class="text-gray-400">Henüz yorum yok. İlk adımı sen at!</p>
                    </div>
                `;
                return;
            }

            commentList.innerHTML = comments.map(c => `
                <div class="bg-white p-5 rounded-2xl border border-gray-100 shadow-sm hover:shadow-md transition-all">
                    <div class="flex justify-between items-start mb-3">
                        <div class="flex items-center gap-3">
                            <div class="w-10 h-10 rounded-full bg-indigo-100 flex items-center justify-center text-indigo-600 font-bold">
                                ${c.userName ? c.userName.charAt(0).toUpperCase() : '?'}
                            </div>
                            <div>
                                <h3 class="font-bold text-gray-800">${c.userName || 'Anonim'}</h3>
                                <p class="text-[10px] text-gray-400 uppercase tracking-wider">${formatDate(c.createdAt)}</p>
                            </div>
                        </div>
                    </div>
                    <p class="text-gray-600 leading-relaxed pl-1">${c.text}</p>
                </div>
            `).join('');
        }

        function formatDate(ts) {
            if (!ts) return "Az önce";
            const date = ts.toDate();
            return date.toLocaleDateString('tr-TR', { day: '2-digit', month: 'long', hour: '2-digit', minute: '2-digit' });
        }

        function showError(msg) {
            errorAlert.textContent = msg;
            errorAlert.classList.remove('hidden');
        }

        // Submit Comment
        commentForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            if (!currentUser) return showError("Oturum açılmadı.");

            const name = document.getElementById('nameInput').value.trim();
            const text = document.getElementById('textInput').value.trim();

            if (!name || !text) return;

            submitBtn.disabled = true;
            submitBtn.textContent = "Gönderiliyor...";

            try {
                const commentsRef = collection(db, 'artifacts', appId, 'public', 'data', 'comments');
                await addDoc(commentsRef, {
                    userName: name,
                    text: text,
                    userId: currentUser.uid,
                    createdAt: serverTimestamp()
                });
                document.getElementById('textInput').value = '';
            } catch (err) {
                showError("Yorum gönderilirken hata oluştu.");
            } finally {
                submitBtn.disabled = false;
                submitBtn.innerHTML = `<span>Yorumu Paylaş</span>`;
            }
        });

        window.onload = initAuth;
    </script>
</head>
<body class="bg-slate-50 min-h-screen text-slate-900 font-sans antialiased">

    <div class="max-w-2xl mx-auto px-4 py-12">
        <!-- Header -->
        <header class="text-center mb-10">
            <div class="inline-flex items-center justify-center w-16 h-16 bg-indigo-600 rounded-2xl shadow-xl shadow-indigo-100 mb-4">
                <svg xmlns="http://www.w3.org/2000/svg" class="w-8 h-8 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z" />
                </svg>
            </div>
            <h1 class="text-3xl font-extrabold text-slate-800 tracking-tight">Yorum Duvarı</h1>
            <p class="text-slate-500 mt-2">Düşüncelerini bırak, burada sonsuza kadar kalsın.</p>
        </header>

        <!-- Error Area -->
        <div id="errorAlert" class="hidden mb-6 p-4 bg-red-50 border border-red-100 text-red-600 rounded-xl text-sm font-medium text-center"></div>

        <!-- Form Area -->
        <section class="bg-white rounded-3xl shadow-sm border border-slate-200 p-6 md:p-8 mb-10">
            <form id="commentForm" class="space-y-5">
                <div>
                    <label class="block text-xs font-bold text-slate-400 uppercase tracking-widest mb-2 ml-1">İsminiz</label>
                    <input id="nameInput" type="text" required placeholder="Adınız nedir?" 
                        class="w-full px-5 py-3.5 bg-slate-50 border border-slate-200 rounded-2xl focus:ring-2 focus:ring-indigo-500 focus:bg-white outline-none transition-all">
                </div>
                <div>
                    <label class="block text-xs font-bold text-slate-400 uppercase tracking-widest mb-2 ml-1">Mesajınız</label>
                    <textarea id="textInput" required rows="3" placeholder="Neler düşünüyorsun?" 
                        class="w-full px-5 py-3.5 bg-slate-50 border border-slate-200 rounded-2xl focus:ring-2 focus:ring-indigo-500 focus:bg-white outline-none transition-all resize-none"></textarea>
                </div>
                <button id="submitBtn" type="submit" 
                    class="w-full bg-indigo-600 hover:bg-indigo-700 text-white font-bold py-4 rounded-2xl shadow-lg shadow-indigo-100 transition-all active:scale-[0.98] flex items-center justify-center gap-2">
                    <span>Yorumu Paylaş</span>
                </button>
            </form>
        </section>

        <!-- Comments List -->
        <section>
            <div class="flex items-center gap-4 mb-6">
                <h2 class="text-xl font-bold text-slate-800">Son Paylaşımlar</h2>
                <div class="h-px flex-1 bg-slate-200"></div>
            </div>
            
            <div id="commentList" class="space-y-4">
                <!-- Comments will be injected here -->
                <div class="text-center py-10">
                    <div class="inline-block w-8 h-8 border-4 border-indigo-200 border-t-indigo-600 rounded-full animate-spin"></div>
                </div>
            </div>
        </section>

        <!-- Footer -->
        <footer class="mt-16 text-center text-slate-400 text-xs">
            <p>&copy; 2024 Kalıcı Yorum Duvarı. Tüm veriler veritabanında saklanır.</p>
        </footer>
    </div>

</body>
</html>

