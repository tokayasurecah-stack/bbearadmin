<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>BBEAR Admin</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
<style>
  :root {
    --bg: #0a0a0a;
    --bg-2: #111;
    --bg-3: #171717;
    --bg-4: #1c1c1c;
    --border: #262626;
    --border-2: #333;
    --text: #ededed;
    --text-dim: #888;
    --text-mute: #555;
    --primary: #4CAF50;
    --primary-hover: #5cc061;
    --danger: #ef4444;
    --warning: #f59e0b;
    --info: #3b82f6;
    --success: #22c55e;
    --radius: 8px;
    --radius-lg: 12px;
    --shadow: 0 4px 16px rgba(0,0,0,0.4);
  }

  * { box-sizing: border-box; margin: 0; padding: 0; }

  html, body { height: 100%; }

  body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    background: var(--bg);
    color: var(--text);
    font-size: 14px;
    line-height: 1.5;
    -webkit-font-smoothing: antialiased;
  }

  code, .mono { font-family: 'JetBrains Mono', monospace; }

  /* ============ LOGIN ============ */
  #loginView {
    display: flex;
    align-items: center;
    justify-content: center;
    min-height: 100vh;
    padding: 24px;
    background: radial-gradient(circle at 50% 0%, #1a1a1a, #0a0a0a 60%);
  }

  .login-box {
    background: var(--bg-2);
    padding: 40px 36px;
    border-radius: var(--radius-lg);
    border: 1px solid var(--border);
    box-shadow: var(--shadow);
    width: 100%;
    max-width: 420px;
  }

  .login-logo {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 28px;
  }

  .logo-mark {
    width: 40px;
    height: 40px;
    background: var(--primary);
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
    color: #000;
    font-size: 18px;
  }

  .login-logo h1 {
    font-size: 20px;
    font-weight: 700;
    letter-spacing: -0.02em;
  }

  .login-logo p {
    font-size: 12px;
    color: var(--text-dim);
  }

  .field {
    margin-bottom: 16px;
  }

  .field label {
    display: block;
    font-size: 12px;
    color: var(--text-dim);
    margin-bottom: 6px;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    font-weight: 500;
  }

  .field-input-wrap {
    display: flex;
    gap: 8px;
  }

  input, select, textarea {
    width: 100%;
    background: var(--bg-3);
    color: var(--text);
    border: 1px solid var(--border);
    padding: 11px 14px;
    border-radius: var(--radius);
    font-size: 14px;
    font-family: inherit;
    transition: border-color 0.15s, background 0.15s;
  }

  input:focus, select:focus, textarea:focus {
    outline: none;
    border-color: var(--primary);
    background: var(--bg-4);
  }

  input::placeholder { color: var(--text-mute); }

  .btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 6px;
    padding: 11px 18px;
    border-radius: var(--radius);
    border: none;
    font-family: inherit;
    font-size: 14px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.15s;
    white-space: nowrap;
    text-decoration: none;
  }

  .btn:disabled { opacity: 0.5; cursor: not-allowed; }

  .btn-primary { background: var(--primary); color: #000; }
  .btn-primary:hover:not(:disabled) { background: var(--primary-hover); }

  .btn-secondary {
    background: var(--bg-3);
    color: var(--text);
    border: 1px solid var(--border);
  }
  .btn-secondary:hover:not(:disabled) { background: var(--bg-4); border-color: var(--border-2); }

  .btn-danger { background: var(--danger); color: #fff; }
  .btn-danger:hover:not(:disabled) { background: #dc2626; }

  .btn-ghost {
    background: transparent;
    color: var(--text-dim);
    border: 1px solid var(--border);
  }
  .btn-ghost:hover:not(:disabled) { color: var(--text); border-color: var(--border-2); }

  .btn-sm { padding: 6px 12px; font-size: 12px; }
  .btn-full { width: 100%; }

  /* ============ APP SHELL ============ */
  #appView { display: none; min-height: 100vh; }

  header {
    position: sticky;
    top: 0;
    z-index: 10;
    background: rgba(10,10,10,0.85);
    backdrop-filter: blur(12px);
    border-bottom: 1px solid var(--border);
    padding: 14px 24px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 16px;
  }

  header .brand {
    display: flex;
    align-items: center;
    gap: 12px;
  }

  header .brand h1 {
    font-size: 16px;
    font-weight: 700;
  }

  header .right {
    display: flex;
    align-items: center;
    gap: 16px;
    font-size: 12px;
    color: var(--text-dim);
  }

  .pulse {
    display: inline-block;
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: var(--success);
    margin-right: 6px;
    animation: pulse 2s infinite;
  }

  @keyframes pulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.4; }
  }

  nav {
    display: flex;
    gap: 4px;
    padding: 12px 24px;
    background: var(--bg-2);
    border-bottom: 1px solid var(--border);
    overflow-x: auto;
  }

  nav button {
    background: transparent;
    color: var(--text-dim);
    border: none;
    padding: 8px 16px;
    border-radius: var(--radius);
    cursor: pointer;
    font-family: inherit;
    font-size: 14px;
    font-weight: 500;
    transition: all 0.15s;
    white-space: nowrap;
  }

  nav button:hover { background: var(--bg-3); color: var(--text); }
  nav button.active { background: var(--primary); color: #000; }

  main {
    padding: 24px;
    max-width: 1500px;
    margin: 0 auto;
  }

  .panel { display: none; animation: fadeIn 0.2s; }
  .panel.active { display: block; }

  @keyframes fadeIn {
    from { opacity: 0; transform: translateY(4px); }
    to { opacity: 1; transform: translateY(0); }
  }

  /* ============ CARDS ============ */
  .card {
    background: var(--bg-2);
    border: 1px solid var(--border);
    border-radius: var(--radius-lg);
    padding: 20px;
    margin-bottom: 16px;
  }

  .card h3 {
    font-size: 15px;
    font-weight: 600;
    margin-bottom: 4px;
  }

  .card .hint {
    font-size: 13px;
    color: var(--text-dim);
    margin-bottom: 16px;
  }

  /* ============ STATS ============ */
  .grid-stats {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 12px;
    margin-bottom: 20px;
  }

  .stat {
    background: var(--bg-2);
    padding: 18px 20px;
    border-radius: var(--radius-lg);
    border: 1px solid var(--border);
    position: relative;
    overflow: hidden;
  }

  .stat::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 2px;
    background: var(--primary);
    opacity: 0.5;
  }

  .stat .label {
    font-size: 11px;
    color: var(--text-dim);
    text-transform: uppercase;
    letter-spacing: 0.06em;
    font-weight: 600;
    margin-bottom: 8px;
  }

  .stat .value {
    font-size: 26px;
    font-weight: 700;
    color: var(--text);
    letter-spacing: -0.02em;
    font-family: 'JetBrains Mono', monospace;
  }

  .stat .sub {
    font-size: 12px;
    color: var(--text-mute);
    margin-top: 4px;
  }

  /* ============ ROWS / GRIDS ============ */
  .row {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
    align-items: flex-end;
  }

  .row > * {
    flex: 1;
    min-width: 160px;
  }

  .row > .shrink { flex: 0 0 auto; min-width: 0; }

  /* ============ TABLE ============ */
  .table-wrap {
    overflow-x: auto;
    border-radius: var(--radius);
  }

  table {
    width: 100%;
    border-collapse: collapse;
    font-size: 13px;
  }

  th {
    text-align: left;
    padding: 10px 12px;
    color: var(--text-dim);
    font-weight: 600;
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    background: var(--bg-3);
    white-space: nowrap;
  }

  th:first-child { border-top-left-radius: var(--radius); }
  th:last-child { border-top-right-radius: var(--radius); }

  td {
    padding: 12px;
    border-top: 1px solid var(--border);
    vertical-align: middle;
  }

  tr:hover td { background: var(--bg-3); }

  td .email { font-weight: 500; }

  .actions-cell {
    display: flex;
    gap: 6px;
    flex-wrap: wrap;
  }

  /* ============ BADGES ============ */
  .badge {
    display: inline-flex;
    align-items: center;
    gap: 4px;
    padding: 3px 9px;
    border-radius: 4px;
    font-size: 11px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.03em;
  }

  .badge.green { background: rgba(34,197,94,0.15); color: #4ade80; }
  .badge.red { background: rgba(239,68,68,0.15); color: #f87171; }
  .badge.yellow { background: rgba(245,158,11,0.15); color: #fbbf24; }
  .badge.blue { background: rgba(59,130,246,0.15); color: #60a5fa; }
  .badge.grey { background: rgba(255,255,255,0.05); color: var(--text-dim); }

  /* ============ MESSAGES ============ */
  .msg {
    padding: 12px 16px;
    border-radius: var(--radius);
    margin: 12px 0;
    font-size: 13px;
    border-left: 3px solid;
    display: none;
  }

  .msg.show { display: block; }

  .msg.success { background: rgba(34,197,94,0.1); color: #4ade80; border-color: var(--success); }
  .msg.error { background: rgba(239,68,68,0.1); color: #f87171; border-color: var(--danger); }
  .msg.info { background: rgba(59,130,246,0.1); color: #60a5fa; border-color: var(--info); }
  .msg.warning { background: rgba(245,158,11,0.1); color: #fbbf24; border-color: var(--warning); }

  /* ============ UTILS ============ */
  .muted { color: var(--text-dim); font-size: 13px; }
  .mono { font-family: 'JetBrains Mono', monospace; font-size: 12px; }
  .tag { padding: 2px 8px; background: var(--bg-4); border-radius: 4px; font-size: 11px; }

  /* ============ MODAL ============ */
  dialog {
    background: var(--bg-2);
    color: var(--text);
    border: 1px solid var(--border);
    border-radius: var(--radius-lg);
    padding: 28px;
    max-width: 480px;
    width: 90%;
    box-shadow: 0 20px 60px rgba(0,0,0,0.6);
  }

  dialog::backdrop {
    background: rgba(0,0,0,0.75);
    backdrop-filter: blur(4px);
  }

  dialog h3 {
    margin-bottom: 6px;
    font-size: 17px;
  }

  dialog .hint {
    color: var(--text-dim);
    font-size: 13px;
    margin-bottom: 20px;
  }

  dialog .actions {
    display: flex;
    justify-content: flex-end;
    gap: 8px;
    margin-top: 20px;
  }

  /* ============ SPINNER ============ */
  .spinner {
    display: inline-block;
    width: 14px;
    height: 14px;
    border: 2px solid rgba(255,255,255,0.2);
    border-top-color: var(--primary);
    border-radius: 50%;
    animation: spin 0.7s linear infinite;
  }

  @keyframes spin { to { transform: rotate(360deg); } }

  /* ============ EMPTY STATE ============ */
  .empty {
    text-align: center;
    padding: 48px 24px;
    color: var(--text-mute);
  }

  .empty-icon {
    font-size: 32px;
    margin-bottom: 12px;
    opacity: 0.5;
  }

  /* ============ LOGO ============ */
  .logo-mark-sm {
    width: 32px;
    height: 32px;
    background: var(--primary);
    border-radius: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
    color: #000;
    font-size: 14px;
  }

  @media (max-width: 640px) {
    main { padding: 16px; }
    header, nav { padding: 12px 16px; }
    .grid-stats { grid-template-columns: 1fr 1fr; }
    .stat .value { font-size: 22px; }
  }
</style>
</head>
<body>

<!-- ============ LOGIN ============ -->
<div id="loginView">
  <div class="login-box">
    <div class="login-logo">
      <div class="logo-mark">B</div>
      <div>
        <h1>BBEAR Admin</h1>
        <p>Sign in to manage your app</p>
      </div>
    </div>

    <div class="field">
      <label for="adminKeyInput">Admin Key</label>
      <div class="field-input-wrap">
        <input id="adminKeyInput" type="password" placeholder="Paste your admin key" autocomplete="current-password" />
        <button type="button" class="btn btn-secondary" id="toggleBtn" onclick="toggleKeyVisibility()">Show</button>
      </div>
    </div>

    <button class="btn btn-primary btn-full" onclick="doLogin()" id="loginBtn">
      Sign in
    </button>

    <div id="loginMsg" class="msg"></div>

    <p class="muted" style="margin-top: 24px; font-size: 12px; text-align: center;">
      Connected to <code id="serverUrlDisplay" class="mono"></code>
    </p>
  </div>
</div>

<!-- ============ APP ============ -->
<div id="appView">
  <header>
    <div class="brand">
      <div class="logo-mark-sm">B</div>
      <h1>BBEAR Admin</h1>
    </div>
    <div class="right">
      <span><span class="pulse"></span><span id="refreshInfo">Ready</span></span>
      <button class="btn btn-ghost btn-sm" onclick="refreshAll()" title="Refresh now">↻</button>
      <button class="btn btn-ghost btn-sm" onclick="logout()">Log out</button>
    </div>
  </header>

  <nav>
    <button data-tab="dash" class="active" onclick="showTab('dash')">Dashboard</button>
    <button data-tab="users" onclick="showTab('users')">Users</button>
    <button data-tab="withdrawals" onclick="showTab('withdrawals')">Withdrawals</button>
    <button data-tab="referrals" onclick="showTab('referrals')">Referrals</button>
    <button data-tab="tools" onclick="showTab('tools')">Tools</button>
  </nav>

  <main>

    <!-- DASHBOARD -->
    <section id="tab-dash" class="panel active">
      <div class="grid-stats">
        <div class="stat">
          <div class="label">Total users</div>
          <div class="value" id="sTotalUsers">—</div>
          <div class="sub" id="sTotalUsersSub">registered accounts</div>
        </div>
        <div class="stat">
          <div class="label">Active subscriptions</div>
          <div class="value" id="sActiveUsers">—</div>
          <div class="sub" id="sActiveUsersSub">days remaining &gt; 0</div>
        </div>
        <div class="stat">
          <div class="label">Pending withdrawals</div>
          <div class="value" id="sPendingWd">—</div>
          <div class="sub" id="sPendingWdSub">awaiting payout</div>
        </div>
        <div class="stat">
          <div class="label">Referral earnings</div>
          <div class="value" id="sTotalReferrals">—</div>
          <div class="sub">across all wallets</div>
        </div>
      </div>

      <div id="dashMsg" class="msg"></div>

      <div class="card">
        <h3>Quick actions</h3>
        <p class="hint">Common tasks you might need right now.</p>
        <div class="row">
          <button class="btn btn-primary" onclick="refreshAll()">Refresh everything</button>
          <button class="btn btn-secondary" onclick="showTab('withdrawals')">Review withdrawals</button>
          <button class="btn btn-secondary" onclick="showTab('tools')">Grant days</button>
        </div>
        <label style="display:flex; align-items:center; gap:8px; margin-top:16px; font-size:13px; color:var(--text-dim);">
          <input type="checkbox" id="autoRefresh" checked style="width:auto" />
          <span>Auto-refresh every 30 seconds</span>
        </label>
      </div>

      <div class="card">
        <h3>Recent withdrawals</h3>
        <p class="hint">Latest 5 withdrawal requests</p>
        <div id="recentWd"></div>
      </div>
    </section>

    <!-- USERS -->
    <section id="tab-users" class="panel">
      <div class="card">
        <div class="row">
          <div style="flex:2">
            <label class="muted" style="display:block; margin-bottom:6px; font-size:12px;">Search</label>
            <input id="userSearch" placeholder="Email or phone" oninput="renderUsers()" />
          </div>
          <div>
            <label class="muted" style="display:block; margin-bottom:6px; font-size:12px;">Filter</label>
            <select id="userFilter" onchange="renderUsers()">
              <option value="all">All users</option>
              <option value="active">Active only</option>
              <option value="expired">Expired / none</option>
            </select>
          </div>
          <button class="btn btn-secondary shrink" onclick="loadUsers()">Reload</button>
        </div>
      </div>

      <div class="card">
        <div class="table-wrap">
          <table>
            <thead>
              <tr>
                <th>#</th>
                <th>Email</th>
                <th>Phone</th>
                <th>Status</th>
                <th>Expires</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody id="usersTableBody"></tbody>
          </table>
        </div>
      </div>
    </section>

    <!-- WITHDRAWALS -->
    <section id="tab-withdrawals" class="panel">
      <div class="card">
        <div class="row">
          <div>
            <label class="muted" style="display:block; margin-bottom:6px; font-size:12px;">Filter by status</label>
            <select id="wdFilter" onchange="loadWithdrawals()">
              <option value="">All</option>
              <option value="pending" selected>Pending</option>
              <option value="processing">Processing</option>
              <option value="completed">Completed</option>
              <option value="failed">Failed</option>
            </select>
          </div>
          <button class="btn btn-secondary shrink" onclick="loadWithdrawals()">Reload</button>
          <button class="btn btn-primary shrink" onclick="processBatch()">Process pending batch</button>
        </div>
        <p class="hint" style="margin-top:12px;">
          Batch processing calls NylonPay for every pending request ≥5,000 UGX.
          Successful ones are marked <span class="badge green">completed</span>.
          Failed ones are <span class="badge red">refunded</span> to the user's wallet.
        </p>
      </div>

      <div id="wdMsg" class="msg"></div>

      <div class="card">
        <div class="table-wrap">
          <table>
            <thead>
              <tr>
                <th>#</th>
                <th>Email</th>
                <th>Amount</th>
                <th>Phone</th>
                <th>Network</th>
                <th>Status</th>
                <th>Requested</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody id="wdTableBody"></tbody>
          </table>
        </div>
      </div>
    </section>

    <!-- REFERRALS -->
    <section id="tab-referrals" class="panel">
      <div class="card">
        <h3>Referrals overview</h3>
        <p class="hint">Top referrers ranked by total earnings</p>
        <button class="btn btn-secondary" onclick="loadReferrals()">Reload</button>
      </div>

      <div class="card">
        <div class="table-wrap">
          <table>
            <thead>
              <tr>
                <th>Email</th>
                <th>Referrals</th>
                <th>Total earned</th>
                <th>Current balance</th>
              </tr>
            </thead>
            <tbody id="referralsTableBody"></tbody>
          </table>
        </div>
      </div>
    </section>

    <!-- TOOLS -->
    <section id="tab-tools" class="panel">
      <div class="card">
        <h3>Grant days</h3>
        <p class="hint">Add N days to a user's subscription</p>
        <div class="row">
          <input id="toolGrantEmail" placeholder="user@example.com" />
          <input id="toolGrantDays" type="number" value="34" style="max-width:120px" />
          <input id="toolGrantReason" placeholder="Reason (optional)" />
          <button class="btn btn-primary shrink" onclick="toolGrant()">Grant</button>
        </div>
      </div>

      <div class="card">
        <h3>Set exact expiry</h3>
        <p class="hint">Force a subscription to end at a specific date and time</p>
        <div class="row">
          <input id="toolSetEmail" placeholder="user@example.com" />
          <input id="toolSetDate" type="datetime-local" />
          <button class="btn btn-primary shrink" onclick="toolSet()">Set</button>
        </div>
      </div>

      <div class="card">
        <h3>Reset password</h3>
        <p class="hint">Assign a new password for a user. Keeps their subscription intact.</p>
        <div class="row">
          <input id="toolResetEmail" placeholder="user@example.com" />
          <input id="toolResetPass" type="text" placeholder="New password" />
          <button class="btn btn-primary shrink" onclick="toolReset()">Reset</button>
        </div>
      </div>

      <div class="card">
        <h3>Revoke subscription</h3>
        <p class="hint">Instantly expire a user's subscription (days become 0)</p>
        <div class="row">
          <input id="toolRevokeEmail" placeholder="user@example.com" />
          <button class="btn btn-danger shrink" onclick="toolRevoke()">Revoke</button>
        </div>
      </div>

      <div class="card">
        <h3>Delete user</h3>
        <p class="hint">Permanently remove a user. Cannot be undone.</p>
        <div class="row">
          <input id="toolDeleteEmail" placeholder="user@example.com" />
          <button class="btn btn-danger shrink" onclick="toolDelete()">Delete</button>
        </div>
      </div>

      <div id="toolsMsg" class="msg"></div>
    </section>

  </main>
</div>

<script>
// =====================================================
// CONFIG — EDIT THIS ONE LINE
// =====================================================
const SERVER_URL = "https://bbear-1.onrender.com";
// =====================================================

let adminKey = localStorage.getItem("bbear_admin_key") || "";
let usersCache = [];
let withdrawalsCache = [];
let autoRefreshTimer = null;

// ---------------- AUTH ----------------

function toggleKeyVisibility() {
  const input = document.getElementById("adminKeyInput");
  const btn = document.getElementById("toggleBtn");
  const isPassword = input.type === "password";
  input.type = isPassword ? "text" : "password";
  btn.textContent = isPassword ? "Hide" : "Show";
}

async function doLogin() {
  const key = document.getElementById("adminKeyInput").value.trim();
  if (!key) return showLoginMsg("Enter your admin key", "error");

  const btn = document.getElementById("loginBtn");
  btn.disabled = true;
  btn.innerHTML = '<span class="spinner"></span> Signing in...';

  try {
    const res = await fetch(SERVER_URL + "/admin/users", {
      method: "GET",
      headers: { "X-Admin-Key": key },
    });

    if (res.status === 403) throw new Error("Wrong admin key");
    if (res.status === 500) {
      const body = await res.json().catch(() => ({}));
      throw new Error(body.detail || "Server error — is ADMIN_KEY configured on Render?");
    }
    if (!res.ok) throw new Error("Server error " + res.status);

    usersCache = await res.json();
    adminKey = key;
    localStorage.setItem("bbear_admin_key", key);
    enterApp();
  } catch (e) {
    const msg = e.message || "Unknown error";
    if (msg.includes("Failed to fetch") || msg.includes("NetworkError")) {
      showLoginMsg(
        "Cannot reach " + SERVER_URL + ". Check the URL and that the backend is running.",
        "error"
      );
    } else {
      showLoginMsg(msg, "error");
    }
  } finally {
    btn.disabled = false;
    btn.textContent = "Sign in";
  }
}

function showLoginMsg(text, type) {
  const el = document.getElementById("loginMsg");
  el.className = "msg show " + (type || "info");
  el.textContent = text;
}

function enterApp() {
  document.getElementById("loginView").style.display = "none";
  document.getElementById("appView").style.display = "block";
  refreshAll();
  startAutoRefresh();
}

function logout() {
  localStorage.removeItem("bbear_admin_key");
  adminKey = "";
  location.reload();
}

// ---------------- API ----------------

async function api(path, opts = {}) {
  const headers = { "X-Admin-Key": adminKey, ...(opts.headers || {}) };
  if (opts.body && typeof opts.body === "object") {
    headers["Content-Type"] = "application/json";
    opts.body = JSON.stringify(opts.body);
  }
  const res = await fetch(SERVER_URL + path, { ...opts, headers });
  const text = await res.text();
  let data;
  try { data = text ? JSON.parse(text) : {}; } catch { data = { raw: text }; }
  if (!res.ok) {
    const msg = data.detail || data.message || ("HTTP " + res.status);
    throw new Error(typeof msg === "string" ? msg : JSON.stringify(msg));
  }
  return data;
}

// ---------------- TABS ----------------

function showTab(name) {
  document.querySelectorAll(".panel").forEach((p) => p.classList.remove("active"));
  document.querySelectorAll("nav button").forEach((b) => b.classList.remove("active"));
  document.getElementById("tab-" + name).classList.add("active");
  document.querySelector(`nav button[data-tab="${name}"]`).classList.add("active");

  if (name === "users") loadUsers();
  if (name === "withdrawals") loadWithdrawals();
  if (name === "referrals") loadReferrals();
}

// ---------------- REFRESH ----------------

async function refreshAll() {
  try {
    await Promise.all([loadUsers(), loadWithdrawals()]);
    updateStats();
    document.getElementById("refreshInfo").textContent = "Refreshed " + new Date().toLocaleTimeString();
  } catch (e) {
    setMsg("dashMsg", "Refresh failed: " + e.message, "error");
  }
}

function startAutoRefresh() {
  if (autoRefreshTimer) clearInterval(autoRefreshTimer);
  autoRefreshTimer = setInterval(() => {
    if (document.getElementById("autoRefresh").checked) refreshAll();
  }, 30000);
}

// ---------------- USERS ----------------

async function loadUsers() {
  usersCache = await api("/admin/users");
  renderUsers();
  renderRecentWithdrawals();
}

function renderUsers() {
  const search = document.getElementById("userSearch").value.toLowerCase().trim();
  const filter = document.getElementById("userFilter").value;

  let list = usersCache.slice();
  if (search) {
    list = list.filter(
      (u) =>
        (u.email || "").toLowerCase().includes(search) ||
        (u.phone || "").toLowerCase().includes(search)
    );
  }
  if (filter === "active") list = list.filter((u) => u.days_left > 0);
  if (filter === "expired") list = list.filter((u) => !u.days_left || u.days_left <= 0);

  const tbody = document.getElementById("usersTableBody");
  if (list.length === 0) {
    tbody.innerHTML = `<tr><td colspan="6">
      <div class="empty"><div class="empty-icon">👤</div>No users</div>
    </td></tr>`;
    return;
  }

  tbody.innerHTML = list.map((u) => {
    const active = u.days_left > 0;
    const badge = active
      ? `<span class="badge green">${u.days_left}d left</span>`
      : `<span class="badge red">expired</span>`;
    const expires = u.subscription_end
      ? new Date(u.subscription_end).toLocaleDateString()
      : "—";
    return `
      <tr>
        <td class="mono">${u.id}</td>
        <td class="email">${escapeHtml(u.email)}</td>
        <td class="mono">${escapeHtml(u.phone || "—")}</td>
        <td>${badge}</td>
        <td class="muted">${expires}</td>
        <td>
          <div class="actions-cell">
            <button class="btn btn-secondary btn-sm" onclick="quickGrant('${jsEsc(u.email)}')">+34d</button>
            <button class="btn btn-secondary btn-sm" onclick="quickReset('${jsEsc(u.email)}')">Reset PW</button>
            <button class="btn btn-danger btn-sm" onclick="quickDelete('${jsEsc(u.email)}')">Delete</button>
          </div>
        </td>
      </tr>`;
  }).join("");
}

function renderRecentWithdrawals() {
  const el = document.getElementById("recentWd");
  const recent = withdrawalsCache.slice(0, 5);

  if (recent.length === 0) {
    el.innerHTML = `<div class="empty"><div class="empty-icon">💸</div>No withdrawal requests yet</div>`;
    return;
  }

  el.innerHTML = `<div class="table-wrap"><table>
    <thead><tr><th>Email</th><th>Amount</th><th>Status</th><th>Date</th></tr></thead>
    <tbody>${recent.map((w) => `
      <tr>
        <td>${escapeHtml(w.email)}</td>
        <td class="mono">${w.amount_ugx.toLocaleString()} UGX</td>
        <td>${statusBadge(w.status)}</td>
        <td class="muted">${w.created_at ? new Date(w.created_at).toLocaleString() : "—"}</td>
      </tr>`).join("")}
    </tbody>
  </table></div>`;
}

async function quickGrant(email) {
  const days = prompt(`Grant how many days to ${email}?`, "34");
  if (!days) return;
  try {
    await api(`/admin/grant-days/${encodeURIComponent(email)}`, {
      method: "POST",
      body: { days: parseInt(days, 10), reason: "Admin quick grant" },
    });
    setMsg("dashMsg", `+${days} days granted to ${email}`, "success");
    await loadUsers();
  } catch (e) {
    setMsg("dashMsg", e.message, "error");
  }
}

async function quickReset(email) {
  const pw = prompt(`Set new password for ${email}:`);
  if (!pw) return;
  try {
    await api(`/admin/reset-password/${encodeURIComponent(email)}`, {
      method: "POST",
      body: { new_password: pw },
    });
    setMsg("dashMsg", `Password reset for ${email}`, "success");
  } catch (e) {
    setMsg("dashMsg", e.message, "error");
  }
}

async function quickDelete(email) {
  if (!confirm(`DELETE ${email} permanently? This cannot be undone.`)) return;
  try {
    await api(`/admin/user/${encodeURIComponent(email)}`, { method: "DELETE" });
    setMsg("dashMsg", `Deleted ${email}`, "success");
    await loadUsers();
  } catch (e) {
    setMsg("dashMsg", e.message, "error");
  }
}

// ---------------- WITHDRAWALS ----------------

async function loadWithdrawals() {
  const status = document.getElementById("wdFilter").value;
  const path = status ? `/admin/withdrawals?status=${status}` : "/admin/withdrawals";
  withdrawalsCache = await api(path);

  const tbody = document.getElementById("wdTableBody");
  if (!withdrawalsCache.length) {
    tbody.innerHTML = `<tr><td colspan="8">
      <div class="empty"><div class="empty-icon">💸</div>No withdrawals with this status</div>
    </td></tr>`;
    return;
  }

  tbody.innerHTML = withdrawalsCache.map((w) => {
    const dt = w.created_at ? new Date(w.created_at).toLocaleString() : "—";
    const actions =
      w.status === "pending" || w.status === "processing"
        ? `<div class="actions-cell">
             <button class="btn btn-primary btn-sm" onclick="completeWd(${w.id})">Complete</button>
             <button class="btn btn-danger btn-sm" onclick="failWd(${w.id})">Fail</button>
           </div>`
        : `<span class="muted">—</span>`;
    return `
      <tr>
        <td class="mono">${w.id}</td>
        <td>${escapeHtml(w.email)}</td>
        <td class="mono">${w.amount_ugx.toLocaleString()} UGX</td>
        <td class="mono">${escapeHtml(w.phone)}</td>
        <td>${escapeHtml(w.network)}</td>
        <td>${statusBadge(w.status)}</td>
        <td class="muted">${dt}</td>
        <td>${actions}</td>
      </tr>`;
  }).join("");
}

function statusBadge(status) {
  const map = {
    pending: "yellow",
    processing: "blue",
    completed: "green",
    failed: "red",
  };
  return `<span class="badge ${map[status] || "grey"}">${status}</span>`;
}

async function completeWd(id) {
  const note = prompt("Note (optional):", "Sent via NylonPay") || "";
  try {
    await api(`/admin/withdrawals/${id}/complete`, {
      method: "POST",
      body: { note },
    });
    setMsg("wdMsg", `Withdrawal #${id} marked completed`, "success");
    await loadWithdrawals();
    await loadUsers();
  } catch (e) {
    setMsg("wdMsg", e.message, "error");
  }
}

async function failWd(id) {
  const note = prompt("Reason for failure:", "Failed — refunded") || "";
  if (!confirm(`Mark withdrawal #${id} as failed and refund the user?`)) return;
  try {
    await api(`/admin/withdrawals/${id}/fail`, {
      method: "POST",
      body: { note },
    });
    setMsg("wdMsg", `Withdrawal #${id} failed and refunded`, "success");
    await loadWithdrawals();
  } catch (e) {
    setMsg("wdMsg", e.message, "error");
  }
}

async function processBatch() {
  if (!confirm("Process all pending withdrawals? NylonPay will be called for each one.")) return;
  setMsg("wdMsg", "Processing...", "info");
  try {
    const res = await api("/admin/withdrawals/process-batch", { method: "POST" });
    setMsg("wdMsg", `Processed ${res.processed} requests`, "success");
    await loadWithdrawals();
    await loadUsers();
  } catch (e) {
    setMsg("wdMsg", e.message, "error");
  }
}

// ---------------- REFERRALS ----------------

async function loadReferrals() {
  // Until /admin/wallets exists, derive from users
  const tbody = document.getElementById("referralsTableBody");
  tbody.innerHTML = `<tr><td colspan="4">
    <div class="empty">
      <div class="empty-icon">🎁</div>
      <div>Referral detail view needs <code>/admin/wallets</code> endpoint</div>
      <div class="muted" style="margin-top:8px">Add it to the backend to enable this tab</div>
    </div>
  </td></tr>`;
}

// ---------------- DASHBOARD STATS ----------------

function updateStats() {
  const active = usersCache.filter((u) => u.days_left > 0).length;
  const pending = withdrawalsCache.filter((w) => w.status === "pending").length;
  document.getElementById("sTotalUsers").textContent = usersCache.length;
  document.getElementById("sActiveUsers").textContent = active;
  document.getElementById("sPendingWd").textContent = pending;
  document.getElementById("sTotalReferrals").textContent = "—";
}

// ---------------- TOOLS ----------------

async function toolGrant() {
  const email = document.getElementById("toolGrantEmail").value.trim();
  const days = parseInt(document.getElementById("toolGrantDays").value, 10);
  const reason = document.getElementById("toolGrantReason").value.trim();
  if (!email || !days) return setMsg("toolsMsg", "Email and days are required", "error");
  try {
    const res = await api(`/admin/grant-days/${encodeURIComponent(email)}`, {
      method: "POST",
      body: { days, reason: reason || null },
    });
    setMsg("toolsMsg", `Granted ${days}d to ${email}. Now ${res.days_left}d left.`, "success");
    await loadUsers();
  } catch (e) {
    setMsg("toolsMsg", e.message, "error");
  }
}

async function toolSet() {
  const email = document.getElementById("toolSetEmail").value.trim();
  const dateStr = document.getElementById("toolSetDate").value;
  if (!email || !dateStr) return setMsg("toolsMsg", "Email and date required", "error");
  const iso = new Date(dateStr).toISOString().replace("Z", "");
  try {
    const res = await api(`/admin/set-subscription/${encodeURIComponent(email)}`, {
      method: "POST",
      body: { subscription_end: iso },
    });
    setMsg("toolsMsg", `Set ${email} to expire on ${res.subscription_end}`, "success");
    await loadUsers();
  } catch (e) {
    setMsg("toolsMsg", e.message, "error");
  }
}

async function toolReset() {
  const email = document.getElementById("toolResetEmail").value.trim();
  const pass = document.getElementById("toolResetPass").value;
  if (!email || !pass) return setMsg("toolsMsg", "Email and password required", "error");
  try {
    await api(`/admin/reset-password/${encodeURIComponent(email)}`, {
      method: "POST",
      body: { new_password: pass },
    });
    setMsg("toolsMsg", `Password reset for ${email}`, "success");
    document.getElementById("toolResetPass").value = "";
  } catch (e) {
    setMsg("toolsMsg", e.message, "error");
  }
}

async function toolRevoke() {
  const email = document.getElementById("toolRevokeEmail").value.trim();
  if (!email) return;
  if (!confirm(`Revoke subscription of ${email}?`)) return;
  try {
    await api(`/admin/revoke/${encodeURIComponent(email)}`, { method: "POST" });
    setMsg("toolsMsg", `Revoked ${email}`, "success");
    await loadUsers();
  } catch (e) {
    setMsg("toolsMsg", e.message, "error");
  }
}

async function toolDelete() {
  const email = document.getElementById("toolDeleteEmail").value.trim();
  if (!email) return;
  if (!confirm(`PERMANENTLY DELETE ${email}? This cannot be undone.`)) return;
  try {
    await api(`/admin/user/${encodeURIComponent(email)}`, { method: "DELETE" });
    setMsg("toolsMsg", `Deleted ${email}`, "success");
    await loadUsers();
  } catch (e) {
    setMsg("toolsMsg", e.message, "error");
  }
}

// ---------------- UTILS ----------------

function escapeHtml(s) {
  if (s == null) return "";
  return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
}

function jsEsc(s) {
  return String(s).replace(/'/g, "\\'").replace(/"/g, '\\"');
}

function setMsg(id, text, type) {
  const el = document.getElementById(id);
  if (!el) return;
  el.className = "msg show " + (type || "info");
  el.textContent = text;
  if (type === "success") {
    setTimeout(() => {
      if (el.textContent === text) {
        el.className = "msg";
        el.textContent = "";
      }
    }, 5000);
  }
}

// ---------------- BOOT ----------------

(function boot() {
  document.getElementById("serverUrlDisplay").textContent = SERVER_URL.replace(/^https?:\/\//, "");

  if (adminKey) {
    fetch(SERVER_URL + "/admin/users", { headers: { "X-Admin-Key": adminKey } })
      .then((r) => (r.ok ? r.json() : Promise.reject()))
      .then((data) => {
        usersCache = data;
        enterApp();
      })
      .catch(() => {
        localStorage.removeItem("bbear_admin_key");
        adminKey = "";
      });
  }

  document.getElementById("adminKeyInput").addEventListener("keydown", (e) => {
    if (e.key === "Enter") doLogin();
  });
})();
</script>
</body>
</html>
