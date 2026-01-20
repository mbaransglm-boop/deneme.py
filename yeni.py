import React, { useState, useEffect } from 'react';
import { initializeApp } from 'firebase/app';
import { 
  getFirestore, 
  collection, 
  addDoc, 
  onSnapshot, 
  query, 
  serverTimestamp 
} from 'firebase/firestore';
import { 
  getAuth, 
  signInAnonymously, 
  signInWithCustomToken, 
  onAuthStateChanged 
} from 'firebase/auth';
import { 
  MessageSquare, 
  Send, 
  User, 
  Clock, 
  AlertCircle,
  Heart,
  Share2
} from 'lucide-react';

// Firebase Yapılandırması (Environment'dan gelen config kullanılır)
const firebaseConfig = JSON.parse(__firebase_config);
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const db = getFirestore(app);
const appId = typeof __app_id !== 'undefined' ? __app_id : 'yorum-duvari-v1';

export default function App() {
  const [user, setUser] = useState(null);
  const [comments, setComments] = useState([]);
  const [name, setName] = useState('');
  const [commentText, setCommentText] = useState('');
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);

  // 1. Kimlik Doğrulama (Auth)
  useEffect(() => {
    const initAuth = async () => {
      try {
        if (typeof __initial_auth_token !== 'undefined' && __initial_auth_token) {
          await signInWithCustomToken(auth, __initial_auth_token);
        } else {
          await signInAnonymously(auth);
        }
      } catch (err) {
        console.error("Oturum hatası:", err);
        setError("Oturum açılamadı. Lütfen sayfayı yenileyin.");
      }
    };

    initAuth();
    const unsubscribe = onAuthStateChanged(auth, (currentUser) => {
      setUser(currentUser);
    });

    return () => unsubscribe();
  }, []);

  // 2. Veritabanı Dinleyici (Firestore)
  useEffect(() => {
    if (!user) return;

    // Koleksiyon yolu: artifacts/{appId}/public/data/comments
    const commentsRef = collection(db, 'artifacts', appId, 'public', 'data', 'comments');
    const q = query(commentsRef);

    const unsubscribe = onSnapshot(q, 
      (snapshot) => {
        const data = snapshot.docs.map(doc => ({
          id: doc.id,
          ...doc.data()
        }));
        
        // Tarihe göre sıralama (Yeniden eskiye)
        const sortedData = data.sort((a, b) => {
          const timeA = b.createdAt?.seconds || 0;
          const timeB = a.createdAt?.seconds || 0;
          return timeA - timeB;
        });

        setComments(sortedData);
        setIsLoading(false);
      }, 
      (err) => {
        console.error("Veri çekme hatası:", err);
        setError("Yorumlar yüklenemedi.");
        setIsLoading(false);
      }
    );

    return () => unsubscribe();
  }, [user]);

  // Yorum Gönderme Fonksiyonu
  const handlePostComment = async (e) => {
    e.preventDefault();
    if (!name.trim() || !commentText.trim() || !user) return;

    setIsSubmitting(true);
    try {
      const commentsRef = collection(db, 'artifacts', appId, 'public', 'data', 'comments');
      await addDoc(commentsRef, {
        author: name.trim(),
        text: commentText.trim(),
        uid: user.uid,
        createdAt: serverTimestamp(),
        likes: 0
      });
      setCommentText('');
    } catch (err) {
      setError("Yorum paylaşılamadı.");
    } finally {
      setIsSubmitting(false);
    }
  };

  const formatDate = (timestamp) => {
    if (!timestamp) return "Az önce";
    const date = timestamp.toDate();
    return new Intl.DateTimeFormat('tr-TR', {
      day: 'numeric',
      month: 'long',
      hour: '2-digit',
      minute: '2-digit'
    }).format(date);
  };

  return (
    <div className="min-h-screen bg-slate-50 text-slate-900 selection:bg-indigo-100 p-4 md:p-10 font-sans">
      <div className="max-w-3xl mx-auto">
        
        {/* Header Bölümü */}
        <header className="mb-12 text-center">
          <div className="inline-flex items-center justify-center p-4 bg-indigo-600 rounded-3xl mb-6 shadow-2xl shadow-indigo-200">
            <MessageSquare className="text-white w-10 h-10" />
          </div>
          <h1 className="text-4xl font-black tracking-tight text-slate-800 mb-2">
            Fikir Duvarı
          </h1>
          <p className="text-slate-500 font-medium">
            Herkese açık, kalıcı ve gerçek zamanlı bir paylaşım alanı.
          </p>
        </header>

        {/* Hata Mesajı */}
        {error && (
          <div className="mb-8 p-4 bg-red-50 border border-red-100 rounded-2xl flex items-center gap-3 text-red-600 animate-pulse">
            <AlertCircle className="w-5 h-5 shrink-0" />
            <span className="text-sm font-semibold">{error}</span>
          </div>
        )}

        {/* Yorum Yazma Alanı */}
        <div className="bg-white rounded-[2rem] shadow-sm border border-slate-200 p-6 md:p-8 mb-12 transform transition-all hover:shadow-xl hover:shadow-slate-200/50">
          <form onSubmit={handlePostComment} className="space-y-6">
            <div className="grid grid-cols-1 gap-6">
              <div>
                <label className="block text-xs font-bold text-slate-400 uppercase tracking-widest mb-2 ml-1">Kimin Adına?</label>
                <div className="relative">
                  <User className="absolute left-4 top-1/2 -translate-y-1/2 w-4 h-4 text-slate-400" />
                  <input
                    type="text"
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                    placeholder="Adınız veya Rumuzunuz"
                    className="w-full pl-12 pr-4 py-4 bg-slate-50 border border-slate-200 rounded-2xl focus:ring-2 focus:ring-indigo-500 focus:bg-white outline-none transition-all placeholder:text-slate-300"
                    required
                  />
                </div>
              </div>
              <div>
                <label className="block text-xs font-bold text-slate-400 uppercase tracking-widest mb-2 ml-1">Mesajınız</label>
                <textarea
                  value={commentText}
                  onChange={(e) => setCommentText(e.target.value)}
                  placeholder="Neler söylemek istersiniz?"
                  rows="3"
                  className="w-full px-5 py-4 bg-slate-50 border border-slate-200 rounded-2xl focus:ring-2 focus:ring-indigo-500 focus:bg-white outline-none transition-all resize-none placeholder:text-slate-300"
                  required
                />
              </div>
            </div>
            
            <button
              type="submit"
              disabled={isSubmitting || !user}
              className="group w-full flex items-center justify-center gap-3 py-4 px-6 bg-indigo-600 hover:bg-indigo-700 text-white font-bold rounded-2xl transition-all shadow-lg shadow-indigo-100 active:scale-95 disabled:opacity-50 disabled:cursor-not-allowed"
            >
              {isSubmitting ? (
                <div className="w-5 h-5 border-2 border-white/30 border-t-white rounded-full animate-spin" />
              ) : (
                <>
                  <Send className="w-4 h-4 group-hover:translate-x-1 group-hover:-translate-y-1 transition-transform" />
                  Paylaşımı Gönder
                </>
              )}
            </button>
          </form>
        </div>

        {/* Yorum Listesi */}
        <div className="space-y-6">
          <div className="flex items-center justify-between mb-8">
            <h2 className="text-2xl font-bold text-slate-800 flex items-center gap-3">
              Yorumlar
              <span className="bg-indigo-100 text-indigo-600 text-xs px-3 py-1 rounded-full font-black">
                {comments.length}
              </span>
            </h2>
          </div>

          {isLoading ? (
            <div className="flex flex-col items-center justify-center py-20 opacity-40">
              <div className="w-10 h-10 border-4 border-indigo-200 border-t-indigo-600 rounded-full animate-spin mb-4" />
              <p className="font-medium">Hafıza yükleniyor...</p>
            </div>
          ) : comments.length === 0 ? (
            <div className="text-center py-20 bg-white rounded-[2rem] border border-dashed border-slate-300">
              <p className="text-slate-400 font-medium">Burası biraz sessiz... İlk yorumu sen yap!</p>
            </div>
          ) : (
            <div className="grid gap-6">
              {comments.map((comment) => (
                <div 
                  key={comment.id} 
                  className="group bg-white p-6 rounded-[2rem] border border-slate-100 shadow-sm hover:shadow-md transition-all relative overflow-hidden"
                >
                  <div className="flex items-start justify-between mb-4">
                    <div className="flex items-center gap-3">
                      <div className="w-12 h-12 rounded-2xl bg-gradient-to-br from-indigo-500 to-purple-600 flex items-center justify-center text-white font-black shadow-inner shadow-black/10">
                        {comment.author.charAt(0).toUpperCase()}
                      </div>
                      <div>
                        <h3 className="font-bold text-slate-800 text-lg">{comment.author}</h3>
                        <div className="flex items-center gap-2 text-[10px] text-slate-400 font-bold uppercase tracking-widest">
                          <Clock className="w-3 h-3" />
                          {formatDate(comment.createdAt)}
                        </div>
                      </div>
                    </div>
                    <button className="p-2 hover:bg-slate-50 rounded-xl transition-colors text-slate-300 hover:text-indigo-500">
                      <Share2 className="w-4 h-4" />
                    </button>
                  </div>
                  
                  <p className="text-slate-600 leading-relaxed text-lg pl-1 whitespace-pre-wrap">
                    {comment.text}
                  </p>

                  <div className="mt-6 pt-5 border-t border-slate-50 flex items-center justify-between">
                    <div className="flex items-center gap-4">
                      <button className="flex items-center gap-1.5 text-slate-400 hover:text-rose-500 transition-colors group/btn">
                        <Heart className="w-4 h-4 group-hover/btn:fill-rose-500 transition-all" />
                        <span className="text-xs font-bold">Beğen</span>
                      </button>
                    </div>
                    <span className="text-[10px] text-slate-200 font-mono">ID: {comment.id.slice(0, 8)}</span>
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>

        {/* Footer */}
        <footer className="mt-20 py-10 text-center border-t border-slate-200">
          <p className="text-slate-400 text-sm font-medium">
            &copy; 2024 Fikir Duvarı &bull; Tüm hakları saklıdır.
          </p>
        </footer>
      </div>
    </div>
  );
}

