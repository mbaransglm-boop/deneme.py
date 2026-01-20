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
import { MessageSquare, Send, User, Clock, AlertCircle } from 'lucide-react';

// Firebase yapılandırması ortam değişkenlerinden alınır
const firebaseConfig = JSON.parse(__firebase_config);
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const db = getFirestore(app);
const appId = typeof __app_id !== 'undefined' ? __app_id : 'comment-wall-demo';

export default function App() {
  const [user, setUser] = useState(null);
  const [comments, setComments] = useState([]);
  const [name, setName] = useState('');
  const [newComment, setNewComment] = useState('');
  const [loading, setLoading] = useState(true);
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState(null);

  // 1. Kimlik Doğrulama (Auth) Kurulumu
  useEffect(() => {
    const initAuth = async () => {
      try {
        if (typeof __initial_auth_token !== 'undefined' && __initial_auth_token) {
          await signInWithCustomToken(auth, __initial_auth_token);
        } else {
          await signInAnonymously(auth);
        }
      } catch (err) {
        console.error("Auth error:", err);
        setError("Oturum açılamadı. Lütfen sayfayı yenileyin.");
      }
    };

    initAuth();
    const unsubscribe = onAuthStateChanged(auth, (currentUser) => {
      setUser(currentUser);
    });

    return () => unsubscribe();
  }, []);

  // 2. Veri Dinleme (Firestore) Kurulumu
  useEffect(() => {
    if (!user) return;

    // Kural 1: Belirtilen yolu kullanıyoruz
    const commentsRef = collection(db, 'artifacts', appId, 'public', 'data', 'comments');
    
    // Kural 2: Karmaşık sorgulardan kaçınıyoruz, sıralamayı bellekte yapacağız
    const q = query(commentsRef);

    const unsubscribe = onSnapshot(q, 
      (snapshot) => {
        const fetchedComments = snapshot.docs.map(doc => ({
          id: doc.id,
          ...doc.data()
        }));
        
        // Bellekte tarihe göre sıralama (Yeniden eskiye)
        const sorted = fetchedComments.sort((a, b) => {
          const timeA = b.createdAt?.seconds || 0;
          const timeB = a.createdAt?.seconds || 0;
          return timeA - timeB;
        });

        setComments(sorted);
        setLoading(false);
      }, 
      (err) => {
        console.error("Firestore error:", err);
        setError("Yorumlar yüklenirken bir sorun oluştu.");
        setLoading(false);
      }
    );

    return () => unsubscribe();
  }, [user]);

  // Yorum Gönderme İşlemi
  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!name.trim() || !newComment.trim() || !user) return;

    setSubmitting(true);
    try {
      const commentsRef = collection(db, 'artifacts', appId, 'public', 'data', 'comments');
      await addDoc(commentsRef, {
        userName: name.trim(),
        text: newComment.trim(),
        userId: user.uid,
        createdAt: serverTimestamp()
      });
      setNewComment('');
      // İsmi hafızada tutabiliriz ama yorum alanını temizliyoruz
    } catch (err) {
      console.error("Submit error:", err);
      setError("Yorum gönderilemedi.");
    } finally {
      setSubmitting(false);
    }
  };

  const formatDate = (timestamp) => {
    if (!timestamp) return "Az önce";
    const date = timestamp.toDate();
    return date.toLocaleString('tr-TR', { 
      day: '2-digit', 
      month: 'short', 
      year: 'numeric', 
      hour: '2-digit', 
      minute: '2-digit' 
    });
  };

  return (
    <div className="min-h-screen bg-slate-50 text-slate-900 font-sans p-4 md:p-8">
      <div className="max-w-2xl mx-auto">
        {/* Header */}
        <header className="mb-8 text-center">
          <div className="inline-flex items-center justify-center p-3 bg-blue-600 rounded-2xl mb-4 shadow-lg shadow-blue-200">
            <MessageSquare className="text-white w-8 h-8" />
          </div>
          <h1 className="text-3xl font-bold tracking-tight text-slate-800">Genel Yorum Duvarı</h1>
          <p className="text-slate-500 mt-2">Düşüncelerini paylaş, kalıcı olsun.</p>
        </header>

        {/* Error Message */}
        {error && (
          <div className="mb-6 p-4 bg-red-50 border border-red-100 rounded-xl flex items-start gap-3 text-red-700">
            <AlertCircle className="w-5 h-5 mt-0.5 flex-shrink-0" />
            <p className="text-sm font-medium">{error}</p>
          </div>
        )}

        {/* Comment Form */}
        <div className="bg-white rounded-2xl shadow-sm border border-slate-200 p-6 mb-8">
          <form onSubmit={handleSubmit} className="space-y-4">
            <div>
              <label className="block text-sm font-semibold text-slate-700 mb-1.5">İsminiz</label>
              <div className="relative">
                <User className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-slate-400" />
                <input
                  type="text"
                  value={name}
                  onChange={(e) => setName(e.target.value)}
                  placeholder="Adınızı yazın..."
                  className="w-full pl-10 pr-4 py-2.5 bg-slate-50 border border-slate-200 rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-transparent outline-none transition-all"
                  required
                />
              </div>
            </div>
            <div>
              <label className="block text-sm font-semibold text-slate-700 mb-1.5">Yorumunuz</label>
              <textarea
                value={newComment}
                onChange={(e) => setNewComment(e.target.value)}
                placeholder="Neler düşünüyorsunuz?"
                rows="3"
                className="w-full px-4 py-3 bg-slate-50 border border-slate-200 rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-transparent outline-none transition-all resize-none"
                required
              />
            </div>
            <button
              type="submit"
              disabled={submitting || !user}
              className={`w-full flex items-center justify-center gap-2 py-3 px-6 rounded-xl font-bold text-white transition-all transform active:scale-95 ${
                submitting || !user 
                ? 'bg-slate-300 cursor-not-allowed' 
                : 'bg-blue-600 hover:bg-blue-700 shadow-md hover:shadow-lg'
              }`}
            >
              {submitting ? (
                <div className="w-5 h-5 border-2 border-white/30 border-t-white rounded-full animate-spin" />
              ) : (
                <>
                  <Send className="w-4 h-4" />
                  Yorumu Gönder
                </>
              )}
            </button>
          </form>
        </div>

        {/* Comments List */}
        <div className="space-y-4">
          <div className="flex items-center justify-between px-2">
            <h2 className="text-lg font-bold text-slate-800 flex items-center gap-2">
              Son Yorumlar
              <span className="bg-slate-200 text-slate-600 text-xs px-2 py-0.5 rounded-full">
                {comments.length}
              </span>
            </h2>
          </div>

          {loading ? (
            <div className="text-center py-12">
              <div className="inline-block w-8 h-8 border-3 border-blue-600/20 border-t-blue-600 rounded-full animate-spin mb-4"></div>
              <p className="text-slate-500 text-sm">Yorumlar yükleniyor...</p>
            </div>
          ) : comments.length === 0 ? (
            <div className="bg-white rounded-2xl border border-dashed border-slate-300 p-12 text-center">
              <p className="text-slate-400">Henüz yorum yapılmamış. İlk yorumu sen yap!</p>
            </div>
          ) : (
            comments.map((comment) => (
              <div 
                key={comment.id} 
                className="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm hover:shadow-md transition-shadow group"
              >
                <div className="flex items-start justify-between mb-2">
                  <div className="flex items-center gap-2">
                    <div className="w-8 h-8 rounded-full bg-blue-100 flex items-center justify-center text-blue-600 font-bold text-sm uppercase">
                      {comment.userName.charAt(0)}
                    </div>
                    <span className="font-bold text-slate-800">{comment.userName}</span>
                  </div>
                  <div className="flex items-center gap-1.5 text-xs text-slate-400 bg-slate-50 px-2 py-1 rounded-lg">
                    <Clock className="w-3 h-3" />
                    {formatDate(comment.createdAt)}
                  </div>
                </div>
                <p className="text-slate-600 leading-relaxed whitespace-pre-wrap pl-10">
                  {comment.text}
                </p>
                <div className="mt-3 pt-3 border-t border-slate-50 flex justify-end">
                   <span className="text-[10px] text-slate-300 font-mono">ID: {comment.userId?.slice(0, 8)}</span>
                </div>
              </div>
            ))
          )}
        </div>
      </div>
    </div>
  );
}

