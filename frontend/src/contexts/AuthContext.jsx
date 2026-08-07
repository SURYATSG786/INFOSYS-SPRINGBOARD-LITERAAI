import { createContext, useContext, useEffect, useState } from 'react';
import api from '../api/client';
import { setAppLanguage, setLearningLanguage } from '../i18n';

const AuthContext = createContext(null);

export function AuthProvider({ children }) {
  const [user, setUser] = useState(null);
  const [token, setToken] = useState(() => localStorage.getItem('literaai_token'));
  const [loading, setLoading] = useState(true);
  const [justLoggedIn, setJustLoggedIn] = useState(false);

  useEffect(() => {
    let alive = true;
    async function boot() {
      if (!token) {
        setLoading(false);
        return;
      }
      try {
        const { user: me } = await api.me();
        if (!alive) return;
        setUser(me);
        const uiLang = me.ui_language || me.preferred_language || 'en';
        const learnLang = me.preferred_language || 'en';
        await setAppLanguage(uiLang);
        setLearningLanguage(learnLang);
      } catch {
        localStorage.removeItem('literaai_token');
        setToken(null);
        setUser(null);
      } finally {
        if (alive) setLoading(false);
      }
    }
    boot();
    return () => { alive = false; };
  }, [token]);

  async function login(email, password) {
    const data = await api.login({ email, password });
    localStorage.setItem('literaai_token', data.token);
    setToken(data.token);
    setUser(data.user);
    const uiLang = data.user.ui_language || data.user.preferred_language || 'en';
    const learnLang = data.user.preferred_language || 'en';
    await setAppLanguage(uiLang);
    setLearningLanguage(learnLang);
    setJustLoggedIn(true);
    return data.user;
  }

  async function register(payload) {
    const data = await api.register(payload);
    localStorage.setItem('literaai_token', data.token);
    setToken(data.token);
    setUser(data.user);
    const uiLang = payload.ui_language || payload.preferred_language || 'en';
    const learnLang = payload.preferred_language || 'en';
    await setAppLanguage(uiLang);
    setLearningLanguage(learnLang);
    setJustLoggedIn(true);
    return data.user;
  }

  async function updateLanguages({ ui_language, preferred_language }) {
    if (!user) return;
    const updates = {};
    if (ui_language) updates.ui_language = ui_language;
    if (preferred_language) updates.preferred_language = preferred_language;

    const res = await api.updateMe(updates);
    const updatedUser = res.user || res;
    setUser(updatedUser);

    const newUi = updatedUser.ui_language || updatedUser.preferred_language;
    if (newUi) await setAppLanguage(newUi);
    if (updatedUser.preferred_language) setLearningLanguage(updatedUser.preferred_language);
    return updatedUser;
  }

  function logout() {
    localStorage.removeItem('literaai_token');
    setToken(null);
    setUser(null);
    setJustLoggedIn(false);
  }

  function refreshUser(next) {
    setUser(next);
  }

  function clearJustLoggedIn() {
    setJustLoggedIn(false);
  }

  return (
    <AuthContext.Provider
      value={{
        user,
        token,
        loading,
        login,
        register,
        logout,
        refreshUser,
        updateLanguages,
        setUser,
        justLoggedIn,
        clearJustLoggedIn
      }}
    >
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  const ctx = useContext(AuthContext);
  if (!ctx) throw new Error('useAuth must be used within AuthProvider');
  return ctx;
}

