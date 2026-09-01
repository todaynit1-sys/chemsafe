# -*- coding: utf-8 -*-
"""한국화학안전협회 정적 사이트 생성기 (1회용).
HTML을 직접 수정한 뒤에는 다시 실행하지 말 것 — 수정분이 덮어써집니다."""
import io, os

NAV = [
    ("index.html",     "홈"),
    ("about.html",     "협회 소개"),
    ("business.html",  "주요 사업"),
    ("education.html", "안전교육"),
    ("ai-center.html", "AI 교육센터"),
    ("member.html",    "회원 안내"),
    ("contact.html",   "오시는 길"),
]

def head(title, desc, cur):
    return f'''<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | 한국화학안전협회</title>
<meta name="description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="한국화학안전협회">
<meta property="og:title" content="{title} | 한국화학안전협회">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="images/og.png">
<meta property="og:locale" content="ko_KR">
<meta name="theme-color" content="#1C95B7">
<link rel="icon" href="images/favicon.svg" type="image/svg+xml">
<link rel="alternate icon" href="images/favicon.png">
<link rel="preconnect" href="https://cdn.jsdelivr.net" crossorigin>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable.min.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/sun-typeface/SUIT@2/fonts/variable/woff2/SUIT-Variable.css">
<link rel="stylesheet" href="assets/style.css">
</head>
<body class="p-{cur.replace(".html","")}">
{header(cur)}
<main>
'''

def header(cur):
    def items(cls):
        out=[]
        for href,label in NAV:
            a=' aria-current="page"' if href==cur else ''
            out.append(f'<a href="{href}"{a}>{label}</a>')
        return out
    nav = "".join(f'<li>{x}</li>' for x in items('nav'))
    drw = "".join(items('drawer'))
    return f'''<header class="hd">
  <div class="wrap hd__top">
    <a class="logo" href="index.html">
      <img class="sig" src="images/logo.svg" width="404" height="92" alt="한국화학안전협회">
    </a>
    <div class="hd__right">
      <a class="hd__tel" href="tel:1644-9049"><b>1644-9049</b><span>평일 09:00 ~ 18:00</span></a>
      <a class="mini" href="https://edu.chemsafe.or.kr/" target="_blank" rel="noopener">수강신청</a>
      <button class="burger" id="burger" aria-label="메뉴 열기" aria-expanded="false" aria-controls="drawer"><i></i></button>
    </div>
  </div>
  <nav class="nav" aria-label="주요 메뉴"><div class="wrap" style="padding-inline:0"><ul>{nav}</ul></div></nav>
  <nav class="drawer" id="drawer" aria-label="모바일 메뉴">{drw}</nav>
</header>'''

FOOT = '''</main>

<footer class="ft">
  <img class="ft__mark" src="images/mark-white.svg" alt="" aria-hidden="true">
  <div class="wrap ft__in">
    <img class="ft__logo" src="images/logo-light.svg" width="404" height="92" alt="한국화학안전협회">
    <span>상호명 : 한국화학안전협회 &nbsp;|&nbsp; 사업자등록번호 : 119-82-82374 &nbsp;|&nbsp; 대표자명 : 지의상</span>
    <span>주소 : 경기도 안산시 단원구 고잔1길 76 리치프라자 401~2호 &nbsp;|&nbsp; Tel : 1644-9049(代) &nbsp;|&nbsp; 031-410-2991~2 &nbsp;|&nbsp; Fax : 031-410-2994</span>
    <span>교육장 : 경기도 안산시 단원구 동산로 63, 3층 &nbsp;|&nbsp; 교육 문의 : 031-410-2992 &nbsp;|&nbsp; chem.edu@chemsafe.or.kr</span>
    <p class="ft__nav"><a href="https://www.chemsafe.or.kr/" target="_blank" rel="noopener">협회 공식 홈페이지</a> &nbsp;·&nbsp; <a href="about.html">협회 소개</a> &nbsp;·&nbsp; <a href="contact.html">찾아오시는 길</a> &nbsp;·&nbsp; <a href="https://www.chemsafe.or.kr/prcenter/notice.html" target="_blank" rel="noopener">공지사항</a> &nbsp;·&nbsp; <a href="https://www.chemsafe.or.kr/prcenter/qna.html" target="_blank" rel="noopener">온라인 문의</a> &nbsp;·&nbsp; <a href="https://edu.chemsafe.or.kr/" target="_blank" rel="noopener">교육시스템</a></p>
    <p class="copy">COPYRIGHT ⓒ 사단법인한국화학안전협회. ALL RIGHTS RESERVED</p>
    <p class="disc">본 페이지는 공식 홈페이지의 공개 정보를 바탕으로 제작한 소개 페이지 시안입니다.</p>
  </div>
</footer>

<nav class="bar" aria-label="빠른 실행">
  <a href="tel:1644-9049">전화 문의</a>
  <a class="pri" href="https://edu.chemsafe.or.kr/" target="_blank" rel="noopener">수강신청</a>
</nav>

<script src="assets/app.js"></script>
</body>
</html>
'''

def phero(bc, title, lead=""):
    p = f'<p>{lead}</p>' if lead else ''
    return f'''  <section class="phero netfx">
    <img class="phero__mark" src="images/mark-white.svg" alt="" aria-hidden="true">
    <div class="wrap">
      <p class="bc">{bc}</p>
      <h1>{title}</h1>
      {p}
    </div>
  </section>
'''

def kick(t):
    return f'<p class="kicker"><img src="images/mark.svg" alt="">{t}</p>'

def write(path, title, desc, body):
    io.open(path,'w',encoding='utf-8').write(head(title,desc,path)+body+FOOT)
    print(path, len(body))

# ============================== index.html ==============================
write("index.html","홈",
"사단법인 한국화학안전협회. 화학물질 취급 사업장의 안전관리를 위한 법정 안전교육, 환경·화학 인허가 컨설팅, 안전진단을 수행하며 AI특화 공동훈련센터를 운영합니다.",
f'''  <section class="kv">
    <div class="wrap kv__in">
      <img class="kv__logo" src="images/logo-light.svg" width="404" height="92" alt="한국화학안전협회">
      <h1><span>우리나라 화학안전 및 산업안전</span><span>한국화학안전협회가 <em>함께 하겠습니다</em></span></h1>
      <p class="kv__sub">환경부 소관 비영리 법인으로 화학물질 취급 사업장의 사고예방을 위한 법정 안전교육과 안전진단, 환경·화학 인허가 컨설팅을 수행합니다.</p>
      <div class="gates">
        <a class="gate" href="about.html">
          <span class="gate__ico"><img src="images/icon.svg" alt=""></span>
          <span><b>협회 소개</b><span>설립목적 · 연혁 · 주요 사업 · 안전교육</span></span>
          <span class="arw">&rsaquo;</span>
        </a>
        <a class="gate gate--ai" href="ai-center.html">
          <span class="gate__ico"><img src="images/icon.svg" alt=""></span>
          <span><b>AI특화 공동훈련센터</b><span>AX 교육 6개 과정 · 협약 기업 전액 무료</span></span>
          <span class="arw">&rsaquo;</span>
        </a>
      </div>
    </div>
  </section>

  <section class="desig">
    <div class="wrap">
      <ul>
        <li><span class="dot"></span><span><b>환경부 유해화학물질 안전교육 전문기관</b><span>지정번호 제2018-001호</span></span></li>
        <li><span class="dot"></span><span><b>노동부 근로자안전보건교육기관</b><span>지정번호 제2020-180022호</span></span></li>
        <li><span class="dot"></span><span><b>노동부 직무교육위탁기관</b><span>지정번호 제2021-190001호</span></span></li>
        <li><span class="dot"></span><span><b>환경부 장외영향평가서 작성 전문기관</b><span>지정번호 ORA-AT-2015-037</span></span></li>
      </ul>
    </div>
  </section>

  <section class="sec">
    <div class="wrap">
      <div class="sec__head">
        {kick("주요 안내")}
        <h2>무엇을 찾으시나요</h2>
      </div>
      <div class="entries">
        <a class="entry alt" href="education.html">
          <span class="no">SERVICE 01</span>
          <h3>법정 안전교육</h3>
          <p>유해화학물질 안전교육과 산업안전보건 교육. 교육과정, 대상, 시간과 신청 절차를 안내합니다.</p>
          <ul><li>유해화학물질 안전교육 5개 과정</li><li>산업안전보건 정기교육 · 관리감독자 교육</li><li>인터넷 원격교육</li></ul>
          <span class="go">안전교육 보기 &rsaquo;</span>
        </a>
        <a class="entry alt" href="business.html">
          <span class="no">SERVICE 02</span>
          <h3>협회 주요 사업</h3>
          <p>화학사고예방관리계획서부터 안전진단까지, 사업장이 이행해야 할 법정 업무 여섯 가지를 지원합니다.</p>
          <ul><li>화학사고예방관리계획서 · PSM</li><li>안전진단 (명령진단 · 자율진단)</li><li>환경·화학 인허가 컨설팅</li></ul>
          <span class="go">주요 사업 보기 &rsaquo;</span>
        </a>
        <a class="entry" href="ai-center.html">
          <span class="no">SERVICE 03</span>
          <h3>AI특화 공동훈련센터</h3>
          <p>규제 대응 업무의 AI 기반 전환(AX)을 지원합니다. 협약 기업은 진단부터 코칭까지 전액 무료입니다.</p>
          <ul><li>진단 · 교육 · 현장적용 · 확산 4단계</li><li>화학 · 안전 · 환경 6개 과정</li><li>협약 체결부터 수료까지 6단계</li></ul>
          <span class="go">AI 교육센터 보기 &rsaquo;</span>
        </a>
        <a class="entry" href="member.html">
          <span class="no">SERVICE 04</span>
          <h3>회원 안내</h3>
          <p>회원 사업장에 제공하는 정보 서비스와 업무 대행·위탁, 안전교육 지원 내용을 안내합니다.</p>
          <ul><li>화학안전 정보 · 자료 제공</li><li>MSDS · PSM 등 업무 대행</li><li>맞춤형 안전교육 지원</li></ul>
          <span class="go">회원 안내 보기 &rsaquo;</span>
        </a>
      </div>
    </div>
  </section>

  <section class="sec sec--tint">
    <div class="wrap">
      <div class="sec__head">
        {kick("협회 소식")}
        <h2>공지사항 · 자료실</h2>
      </div>
      <div class="news">
        <a href="https://www.chemsafe.or.kr/prcenter/notice.html" target="_blank" rel="noopener">
          <span><span class="cat">공지사항</span><span class="nt">[안내공고 제2026-007호] AI 특화 공동훈련센터 LMS 구축</span></span><span class="ar">&rsaquo;</span><span class="date">2026.07.10</span></a>
        <a href="https://www.chemsafe.or.kr/prcenter/notice.html" target="_blank" rel="noopener">
          <span><span class="cat">공지사항</span><span class="nt">[AI특화공동훈련센터] AI 전환(AX) 교육 및 도입지원 안내</span></span><span class="ar">&rsaquo;</span><span class="date">2026.07.08</span></a>
        <a href="https://www.chemsafe.or.kr/prcenter/notice.html" target="_blank" rel="noopener">
          <span><span class="cat">공지사항</span><span class="nt">[안내공고 제2026-006호] 교육장 교육장비 구매 및 설치</span></span><span class="ar">&rsaquo;</span><span class="date">2026.06.22</span></a>
        <a href="https://www.chemsafe.or.kr/prcenter/notice.html" target="_blank" rel="noopener">
          <span><span class="cat">공지사항</span><span class="nt">[안내공고 제2026-005호] 교육장 방송장비 구매 및 설치</span></span><span class="ar">&rsaquo;</span><span class="date">2026.06.19</span></a>
        <a href="https://www.chemsafe.or.kr/prcenter/notice.html" target="_blank" rel="noopener">
          <span><span class="cat">공지사항</span><span class="nt">2024년 유해화학물질 취급시설 특별 안전교육 지원안내</span></span><span class="ar">&rsaquo;</span><span class="date">2024.06.25</span></a>
      </div>
      <div class="btnrow">
        <a class="btn btn--line" href="https://www.chemsafe.or.kr/prcenter/notice.html" target="_blank" rel="noopener">공지사항</a>
        <a class="btn btn--line" href="https://www.chemsafe.or.kr/prcenter/board.html" target="_blank" rel="noopener">자료실</a>
        <a class="btn btn--line" href="https://www.chemsafe.or.kr/prcenter/photo.html" target="_blank" rel="noopener">포토뉴스</a>
      </div>
      <p class="note">협회 공식 홈페이지 게시판의 최신 게시물입니다 (총 60건). 전체 목록과 새 글은 게시판에서 확인하실 수 있습니다.</p>
    </div>
  </section>

  <section class="sec">
    <div class="wrap">
      <div class="sec__head">
        {kick("자주 찾는 메뉴")}
        <h2>신청 및 문의</h2>
      </div>
      <div class="quick">
        <a href="https://edu.chemsafe.or.kr/" target="_blank" rel="noopener"><span><span class="t">법정 안전교육 수강신청</span><span class="d">교육시스템에서 신청 · 수강 조회 · 수료증 출력</span></span><span class="ar">&rsaquo;</span></a>
        <a href="https://ai.chemsafe.or.kr/" target="_blank" rel="noopener"><span><span class="t">AI 교육센터 수강신청</span><span class="d">협약 기업 조회·신청, 수료증 출력</span></span><span class="ar">&rsaquo;</span></a>
        <a href="https://www.chemsafe.or.kr/prcenter/qna.html" target="_blank" rel="noopener"><span><span class="t">온라인 문의 (Q&amp;A)</span><span class="d">협회 공식 홈페이지 문의 게시판</span></span><span class="ar">&rsaquo;</span></a>
        <a href="tel:1644-9049"><span><span class="t">전화 문의 1644-9049</span><span class="d">평일 09:00~18:00 · 토·일·공휴일 휴무</span></span><span class="ar">&rsaquo;</span></a>
      </div>
    </div>
  </section>
''')

# ============================== about.html ==============================
write("about.html","협회 소개",
"한국화학안전협회는 환경부 소관 비영리 법인으로 화학 안전교육과 안전진단, 시험, 검사, 기술개발과 연구업무를 수행합니다. 회장 인사말과 설립목적, 연혁·지정 현황을 안내합니다.",
phero("협회소개","화학 안전교육과 사고예방에<br>만전을 기하겠습니다","한국화학안전협회는 환경부 소관 비영리 법인입니다.") + f'''
  <section class="sec" id="greeting">
    <div class="wrap">
      <div class="sec__head">
        {kick("회장 인사말")}
        <h2>화학 사업장 안전의<br>중요성을 생각합니다</h2>
      </div>
      <div class="prose measure">
        <p>한국화학안전협회 홈페이지를 방문하여 주셔서 감사합니다.</p>
        <p>2012년 9월 27일 구미공단 불산 유출사고는 국내 최초의 대규모 불산 유출사고이자 유독성 화학물질 유출로는 전례 없는 사고였습니다. 1991년 페놀 유출사고에 이은 최대의 독극물 유출 사고로 5명이 사망하고 500여 명의 환자가 발생하였으며, 인근 90ha에 이르는 농경지에도 큰 피해가 발생하였습니다.</p>
        <p>이러한 화학물질 유출사고는 한 번의 과오에 의해 수백, 수천의 인명과 엄청난 경제적 손실이 유발되는 대형 재난사고로 이어질 수 있다는 사실을 통해, 국민 모두에게 화학 사업장 안전의 중요성과 심각성을 일깨워 주었습니다.</p>
        <p>정부도 화학사고의 심각성을 인식하여 화학물질관리법과 화학물질의 등록 및 평가 등에 관한 법률을 신속히 개정·제정하고 2015년 1월 1일 시행함으로써 선제적인 화학사고 예방 정책을 펴고 있습니다.</p>
        <p>이에 우리 한국화학안전협회는 환경부 소관 비영리 법인으로 화학 안전교육과 안전진단, 시험, 검사, 기술개발과 연구업무를 수행함으로써 화학물질 취급 사업장의 사고예방에 만전을 기하고자 하오니, 적극 성원하여 주시기 바랍니다.</p>
        <p class="sign">회장 지의상<span>한국화학안전협회</span></p>
      </div>
    </div>
  </section>

  <section class="sec sec--soft" id="purpose">
    <div class="wrap">
      <div class="sec__head">
        {kick("설립목적")}
        <h2>무엇을 위해<br>설립되었는가</h2>
      </div>
      <div class="callout">
        <p>한국화학안전협회는 환경보건법, 화학물질관리법 및 산업안전보건법 등에 준하는 산업 현장의 화학 설비 및 화학물질에 대한 안전사고를 예방하기 위한 교육, 진단, 시험 등의 업무를 수행함으로써 인적·물적 및 환경적 피해를 최소화하고, 사전적 예방과 홍보 활동을 통하여 국민 경제 발전에 기여하기 위한 목적으로 설립되었습니다.</p>
      </div>
    </div>
  </section>

  <section class="sec" id="history">
    <div class="wrap">
      <div class="sec__head">
        {kick("연혁 · 지정 현황")}
        <h2>정부가 지정한<br>화학안전 교육기관</h2>
        <p class="sec__sub measure">환경부와 노동부로부터 받은 지정·허가 이력입니다.</p>
      </div>
      <ul class="tl">
        <li><span class="y">2021.04</span><span><span class="t">노동부 직무교육위탁기관 지정</span><span class="no">지정번호 제2021-190001호</span></span></li>
        <li><span class="y">2020.05</span><span><span class="t">노동부 근로자안전보건교육기관 지정</span><span class="no">지정번호 제2020-180022호</span></span></li>
        <li><span class="y">2018.12</span><span><span class="t">환경부 유해화학물질 안전교육 전문기관 지정</span><span class="no">지정번호 제2018-001호</span></span></li>
        <li><span class="y">2015.04</span><span><span class="t">환경부 장외영향평가서 작성 전문기관 지정</span><span class="no">지정번호 ORA-AT-2015-037</span></span></li>
        <li><span class="y">2014.02</span><span><span class="t">환경부 법인 설립허가</span><span class="no">환경부 허가 제477호</span></span></li>
      </ul>
    </div>
  </section>

  <section class="sec sec--tint" id="info">
    <div class="wrap">
      <div class="sec__head">
        {kick("협회 정보")}
        <h2>기본 정보</h2>
      </div>
      <ul class="dl" style="margin-top:0">
        <li><span class="k">상호명</span><span class="v">한국화학안전협회 (사단법인)</span></li>
        <li><span class="k">대표자명</span><span class="v">지의상</span></li>
        <li><span class="k">사업자등록번호</span><span class="v">119-82-82374</span></li>
        <li><span class="k">설립 허가</span><span class="v">2014년 2월 환경부 법인 설립허가 (환경부 허가 제477호)</span></li>
        <li><span class="k">주요 사업</span><span class="v">법정 안전교육 · 안전진단 · 환경·화학 인허가 컨설팅 · 회원 지원 · AI특화 공동훈련센터 운영</span></li>
        <li><span class="k">교육 대상</span><span class="v">화학물질 취급 사업장의 안전·환경·보건 담당자 및 관리감독자</span></li>
        <li><span class="k">대표전화</span><span class="v"><a href="tel:1644-9049">1644-9049</a> (代) · <a href="tel:031-410-2991">031-410-2991~2</a></span></li>
        <li><span class="k">팩스</span><span class="v">031-410-2994</span></li>
      </ul>
      <div class="btnrow">
        <a class="btn btn--line" href="contact.html">오시는 길 보기</a>
        <a class="btn btn--line" href="https://www.chemsafe.or.kr/about/greeting.html" target="_blank" rel="noopener">협회 공식 홈페이지</a>
      </div>
      <ul class="srclist">
        <li><a href="https://www.chemsafe.or.kr/about/greeting.html" target="_blank" rel="noopener">회장인사말</a></li>
        <li><a href="https://www.chemsafe.or.kr/about/history.html" target="_blank" rel="noopener">연혁</a></li>
        <li><a href="https://www.chemsafe.or.kr/about/ci.html" target="_blank" rel="noopener">C.I 소개</a></li>
        <li><a href="https://www.chemsafe.or.kr/about/organ.html" target="_blank" rel="noopener">조직도</a></li>
        <li><a href="https://www.chemsafe.or.kr/about/certificate.html" target="_blank" rel="noopener">인증현황</a></li>
      </ul>
      <p class="note">위 항목은 협회 공식 홈페이지에서 확인하실 수 있습니다.</p>
    </div>
  </section>
''')

# ============================== business.html ==============================
write("business.html","협회 주요 사업",
"화학사고예방관리계획서, 공정안전보고서(PSM), 안전진단, 통합환경 인허가, 환경·화학 인허가(종합), 유해·위험방지계획서 작성 및 컨설팅을 수행합니다.",
phero("협회주요사업","법정 서류부터 진단까지<br>여섯 가지 사업","사업장이 이행해야 할 법정 업무를 진단·작성·컨설팅으로 지원합니다.") + f'''
  <section class="sec">
    <div class="wrap">

      <details class="acc" open>
        <summary><span class="tag">화학사고 대응</span><div class="ttl">화학사고예방관리계획서</div></summary>
        <div class="acc__body">
          <p class="law">화학물질관리법 제23조 (화학사고예방관리계획서의 작성·제출)</p>
          <div>
            <h4>제도란</h4>
            <ul class="bul">
              <li>유해화학물질 취급시설의 안전성을 확보하고, 사고 시 피해를 최소화할 수 있도록 비상대응체계를 구축·운영하도록 하는 제도입니다.</li>
              <li>기존 장외영향평가와 위해관리계획을 통합하여 대체 가능한 내용은 통합·정비하고, 사고 시 외부 영향이 적은 일정 규모 미만 취급사업장은 서류 제출을 면제하여 부담을 완화하였습니다.</li>
              <li>유해화학물질을 다량 취급하는 대규모 사업장을 중심으로 집중 관리합니다.</li>
            </ul>
          </div>
          <div>
            <h4>적용대상 및 구분</h4>
            <p style="font-size:15.5px;line-height:1.8;color:var(--ink-2)">「화학물질관리법」 시행규칙 별표 10 및 환경부 고시 「유독물질, 제한물질, 금지물질 및 허가물질의 규정수량에 관한 규정」에 따른 규정수량 기준 이상의 유해화학물질 취급시설을 설치·운영하려는 자</p>
            <ul class="bul" style="margin-top:12px">
              <li><b>1군 유해화학물질 취급 사업장</b> — 시행규칙 별표 10 및 환경부 고시의 상위 규정수량 이상 취급</li>
              <li><b>2군 유해화학물질 취급 사업장</b> — 하위 규정수량 이상, 상위 규정수량 미만 취급</li>
            </ul>
            <p class="tblnote">※ 단, 법 제23조 제1항 제1호·제2호 및 제3호에 따라 환경부령으로 정하는 일부 사업장은 제출 제외</p>
          </div>
          <div>
            <h4>제출 단위</h4>
            <ul class="bul"><li>제출 구분 — 사업장 단위</li><li>제출 단위 — 사업장 단위 또는 화학사고 예방·대비·대응·복구 운영 단위</li></ul>
          </div>
          <p class="srcrow"><a class="srclink" href="https://www.chemsafe.or.kr/business/business8.html" target="_blank" rel="noopener">협회 공식 페이지에서 원문 보기</a></p>
        </div>
      </details>

      <details class="acc">
        <summary><span class="tag">공정안전</span><div class="ttl">공정안전보고서(PSM) 작성 대행 컨설팅</div></summary>
        <div class="acc__body">
          <p class="law">산업안전보건법 제44조 (공정안전보고서의 작성·제출)</p>
          <div>
            <h4>제출 시기</h4>
            <ul class="bul">
              <li><b>착공일 30일 전</b></li>
              <li>유해·위험물질 제조, 취급, 저장 설비의 설치·이전 시</li>
              <li>주요 구조부분의 변경 시</li>
            </ul>
          </div>
          <div>
            <h4>적용 대상</h4>
            <ul class="bul">
              <li>산업안전보건법 시행령 제43조(공정안전보고서의 제출 대상)에서 규정하는 대상 업종</li>
              <li>동법 시행령 [별표 13]에서 규정하는 유해·위험물질 중 하나 이상을 규정량 이상 제조·취급·저장하는 사업장</li>
            </ul>
          </div>
          <p class="srcrow"><a class="srclink" href="https://www.chemsafe.or.kr/business/business3.html" target="_blank" rel="noopener">협회 공식 페이지에서 원문 보기</a></p>
        </div>
      </details>

      <details class="acc">
        <summary><span class="tag">진단</span><div class="ttl">안전진단</div></summary>
        <div class="acc__body">
          <p class="law">산업안전보건법 제47조 (안전보건진단) · 시행령 제46조</p>
          <div>
            <h4>안전진단이란</h4>
            <p style="font-size:15.5px;line-height:1.8;color:var(--ink-2)">사업장 내 주요 위험 공정 및 시설에 대한 안전관리 실태를 파악하여 안전보건상 잠재된 유해·위험 요인을 진단하고, 그에 대한 개선 대책을 제시하는 일련의 과정입니다.</p>
          </div>
          <div>
            <h4>진단 종류</h4>
            <div class="tblwrap"><table>
              <thead><tr><th>구분</th><th>내용</th></tr></thead>
              <tbody>
                <tr><td><b>명령진단</b></td><td>1. 산업재해율이 같은 업종 평균 산업재해율의 2배 이상인 사업장<br>2. 사업주가 필요한 안전조치 또는 보건조치를 이행하지 아니하여 중대재해가 발생한 사업장<br>3. 직업성 질병자가 연간 2명 이상 발생한 사업장 (상시근로자 1천명 이상 사업장은 3명 이상)<br>4. 그 밖에 작업환경 불량, 화재·폭발 또는 누출사고 등으로 사업장 주변까지 피해가 확대된 사업장</td></tr>
                <tr><td><b>자율진단</b></td><td>사업장 내 유해·위험요인을 제거·관리하고 안전관리체계 이행을 위하여 안전진단기관의 컨설팅을 받아 사업장이 자율적으로 실시하는 안전진단</td></tr>
              </tbody>
            </table></div>
          </div>
          <div>
            <h4>진단 장비</h4>
            <p style="font-size:15.5px;line-height:1.8;color:var(--ink-2)">회전속도측정기, 자동탐상비파괴시험기, 재료강도시험기, 진동측정기, 표준압력계, 절연저항측정기, 만능회로측정기, 산업용내시경, 경도측정기, 산소농도측정기, 두께측정기, 가스농도측정기, 가연성가스검지관, 수압시험기, 접지저항측정기, 계전기기시험기, 정전기전하량측정기, 정전기전위측정기, 차압측정기 등 <b>법정 장비 19종</b>을 보유하고 있습니다.</p>
          </div>
          <div>
            <h4>진단 비용 산정</h4>
            <p style="font-size:15.5px;line-height:1.8;color:var(--ink-2)">엔지니어링산업 진흥법 제31조 제2항에 따라 위험도 및 사업장 규모(근로자수)에 따른 진단일수와 기술자 등급별 최소 진단참여일수를 고려하여 사업장 특성에 적합한 견적금액을 산출합니다. 위험도는 고용노동부 고시 「사업종류별 산재보험료율」을 기준으로 고위험(30 이상)·중위험(15 이상 30 미만)·저위험(15 미만)으로 구분합니다.</p>
            <p class="tblnote">※ 한국화학안전협회는 안전진단사업 시행지침의 최소진단일수를 준용합니다.</p>
          </div>
          <div>
            <h4>자주 묻는 질문</h4>
            <ul class="bul">
              <li><b>비용은 어떻게 산정되나요?</b> 사업장의 규모, 업종, 상시근로자 수 및 협회의 점검 투입인력을 고려하여 산정됩니다. 자세한 문의는 1644-9049 내선 1번으로 연락 주시기 바랍니다.</li>
              <li><b>기간은 얼마나 걸리나요?</b> 진단 기간은 사업장 규모로 결정되며, 결과는 보고서 형태의 책자로 보내드립니다. 보고서 제본은 진단 점검이 끝나고 약 3~4주 소요됩니다.</li>
              <li><b>무엇을 진단하나요?</b> 산업재해·사고의 발생 원인, 작업조건 및 작업방법 평가, 유해·위험요인 측정 및 분석(기계·기구 설비, 폭발성·인화성 물질, 전기·열 에너지, 추락·붕괴·낙하 등), 보호구·안전보건장비 및 작업환경 개선시설의 적정성을 진단합니다.</li>
            </ul>
          </div>
          <p class="srcrow"><a class="srclink" href="https://www.chemsafe.or.kr/business/business4.html" target="_blank" rel="noopener">협회 공식 페이지에서 원문 보기</a></p>
        </div>
      </details>

      <details class="acc">
        <summary><span class="tag">인허가</span><div class="ttl">통합환경 관리법 및 인허가 컨설팅</div></summary>
        <div class="acc__body">
          <p class="law">환경오염시설의 통합관리에 관한 법률</p>
          <div>
            <h4>제도 개요</h4>
            <ul class="bul">
              <li>7개 법률 10개 인·허가·신고를 하나로 통합한 제도입니다.</li>
              <li><b>적용대상</b> — 19개 업종의 대기 또는 수질 1·2종 사업장</li>
              <li><b>적용시기</b> — 2017년 1월 1일부터 5년간 단계적 시행. 기존 사업장은 업종별 시행일로부터 4년간 유예기간 적용</li>
            </ul>
          </div>
          <p class="srcrow"><a class="srclink" href="https://www.chemsafe.or.kr/business/business5.html" target="_blank" rel="noopener">협회 공식 페이지에서 원문 보기</a></p>
        </div>
      </details>

      <details class="acc">
        <summary><span class="tag">인허가</span><div class="ttl">환경·화학 인허가(종합) 작성 및 컨설팅</div></summary>
        <div class="acc__body">
          <p style="font-size:15.5px;line-height:1.8;color:var(--ink-2)">사업장에 필요한 환경·화학 분야 인허가를 한 번에 검토하고 작성·제출까지 지원합니다. 인허가별 근거 법률과 제출 시점은 아래와 같습니다.</p>
          <div class="tblwrap"><table>
            <thead><tr><th>인허가</th><th>근거 법률</th><th>관할</th><th>제출 시점</th><th>처리기한<br>(작성 소요)</th></tr></thead>
            <tbody>
              <tr><td><b>공정안전보고서</b></td><td>산업안전보건법 제44조</td><td>화학사고·중대재해<br>예방센터</td><td>착공 30일 전</td><td>30일 (2~3개월)</td></tr>
              <tr><td><b>화학사고예방<br>관리계획서</b></td><td>화학물질관리법 제23조</td><td>화학물질안전원</td><td>설치검사 60일 전</td><td>30일 (검토기간)</td></tr>
              <tr><td><b>대기배출시설<br>설치(허가)신청</b></td><td>대기환경보전법 제23조</td><td>관할 시·도</td><td>시설 설치 전</td><td>10일 (2주)</td></tr>
              <tr><td><b>폐수배출시설<br>설치(허가)신청</b></td><td>물환경보전법 제33조</td><td>관할 시·도</td><td>시설 설치 전</td><td>10일 (2주)</td></tr>
              <tr><td><b>악취배출시설<br>설치신고</b></td><td>악취방지법 제8조</td><td>관할 시</td><td>시설 설치 전<br>(대기·폐수 완료 후)</td><td>7일 (1주)</td></tr>
              <tr><td><b>유해화학물질<br>영업허가신청</b></td><td>화학물질관리법 제28조</td><td>관할 유역청<br>(방재센터)</td><td>가동 전</td><td>15일 (3주)</td></tr>
            </tbody>
          </table></div>
          <p class="tblnote">표가 잘려 보이면 좌우로 밀어 보실 수 있습니다.</p>
          <p class="srcrow"><a class="srclink" href="https://www.chemsafe.or.kr/business/business6.html" target="_blank" rel="noopener">협회 공식 페이지에서 원문 보기</a></p>
        </div>
      </details>

      <details class="acc">
        <summary><span class="tag">산업안전</span><div class="ttl">유해·위험방지계획서 작성 및 컨설팅</div></summary>
        <div class="acc__body">
          <p class="law">산업안전보건법 제42조 (유해위험방지계획서의 작성·제출 등)</p>
          <div class="callout warn">
            <h3>미제출 시 1,000만원 이하의 과태료</h3>
            <p>사업주는 해당 작업 시작일 15일 전까지 유해·위험방지계획서 2부를 작성하여 공단에 제출하여야 합니다.</p>
          </div>
          <div>
            <h4>적용 대상</h4>
            <ul class="bul">
              <li>산업안전보건법 시행령 제33조의2의 대상 업종</li>
              <li>산업안전보건법 시행규칙 제120조 제1항의 대상 설비</li>
              <li>대상 업종 또는 특정 설비 중 어느 하나에 해당될 경우 제출</li>
            </ul>
            <p class="tblnote">※ 제출 제외 : PSM 대상 공정(설비)</p>
          </div>
          <div>
            <h4>작업 시작의 의미</h4>
            <ul class="bul">
              <li><b>제출 대상 사업장</b> — 공사 시작일(대지 정리 및 가설사무소 설치 등 공사 준비 기간은 제외). 기존공장·임대공장·아파트형공장 등 건설물이 이미 설치되어 있는 경우에는 생산설비 설치 시작일</li>
              <li><b>대상 설비</b> — 대상 설비 설치일</li>
            </ul>
          </div>
          <p class="srcrow"><a class="srclink" href="https://www.chemsafe.or.kr/business/business7.html" target="_blank" rel="noopener">협회 공식 페이지에서 원문 보기</a></p>
        </div>
      </details>

      <div class="btnrow">
        <a class="btn btn--solid" href="tel:1644-9049">사업 문의 1644-9049</a>
        <a class="btn btn--line" href="https://www.chemsafe.or.kr/prcenter/qna.html" target="_blank" rel="noopener">온라인 문의</a>
      </div>
    </div>
  </section>
''')

# ============================== education.html ==============================
write("education.html","안전교육",
"화학물질관리법에 따른 유해화학물질 안전교육과 산업안전보건법에 따른 산업안전보건 교육을 운영합니다. 교육과정, 대상, 시간과 신청 절차를 안내합니다.",
phero("안전교육","법정 안전교육<br>두 가지를 운영합니다","환경부 지정 전문기관(제2018-001호), 노동부 지정 교육기관(제2020-180022호)으로 운영합니다.") + f'''
  <section class="sec" id="chem">
    <div class="wrap">
      <div class="sec__head">
        {kick("유해화학물질 안전교육")}
        <h2>화학물질관리법에 따른<br>법정의무 교육</h2>
      </div>
      <p class="law">화학물질관리법 제33조 (유해화학물질 안전교육)</p>

      <div style="margin-top:26px">
        <h3 style="font-size:19px">교육 목적</h3>
        <ul class="bul" style="margin-top:12px">
          <li>화학사고·테러로 인한 국가와 국민의 재산 및 인명 보호</li>
          <li>화학사고·테러 예방 및 대응 환경전문 인재 양성</li>
          <li>실무자의 완벽한 사고예방·대응과 안전관리체계 확립</li>
          <li>전문·실무 능력 향상을 위한 역량강화 교육 운영과 표준화된 교육·훈련 체계 마련</li>
        </ul>
      </div>

      <div style="margin-top:30px">
        <h3 style="font-size:19px">적용 대상</h3>
        <p style="margin-top:10px;font-size:16px;color:var(--ink-2);line-height:1.8">유해화학물질을 제조·사용·판매·운반하는 사업장 <b>[제2018-001호 지정기관]</b></p>
      </div>

      <div style="margin-top:30px">
        <h3 style="font-size:19px">교육대상별 교육과정</h3>
        <div class="tblwrap"><table>
          <thead><tr><th>과정 구분</th><th>교육 대상</th></tr></thead>
          <tbody>
            <tr><td><b>기술인력 및 관리자<br>(16시간) / 2년</b><br><span style="color:var(--steel);font-size:13.5px">법 제32조 및 법 제28조 제2항</span></td><td>유해화학물질 취급시설 기술인력 및 관리자</td></tr>
            <tr><td><b>취급담당자<br>(16시간) / 2년</b><br><span style="color:var(--steel);font-size:13.5px">영 제13조</span></td><td>유해화학물질 영업자가 고용한 자 중 유해화학물질 직접 취급자<br>수급인과 수급인이 고용한 사람으로 유해화학물질을 직접 취급하는 사람<br>장외영향평가서 작성 담당자 / 위해관리계획서 작성 담당자<br><span style="color:var(--steel);font-size:13.5px">※ 집체교육(16시간) 또는 집체교육(8시간) + 온라인교육(8시간) 택 1</span></td></tr>
            <tr><td><b>취급담당자<br>(8시간) / 2년</b><br><span style="color:var(--steel);font-size:13.5px">영 제13조</span></td><td>유해화학물질을 직접 다루거나 취급시설을 운전·점검함으로 인해 유해화학물질이 인체에 직접 노출될 우려가 있는 취급자</td></tr>
            <tr><td><b>취급시설 없는<br>판매업관리자<br>(8시간) / 2년</b><br><span style="color:var(--steel);font-size:13.5px">법 제27조 제2호</span></td><td>취급시설이 없는 유해화학물질 판매업의 유해화학물질 관리자</td></tr>
            <tr><td><b>운반자 과정<br>(8시간) / 2년</b><br><span style="color:var(--steel);font-size:13.5px">법 제13조 제5호</span></td><td>유해화학물질을 운반하는 자</td></tr>
          </tbody>
        </table></div>
        <p class="tblnote">표가 잘려 보이면 좌우로 밀어 보실 수 있습니다.</p>
      </div>

      <div style="margin-top:34px">
        <h3 style="font-size:19px">교육장 안내</h3>
        <div class="grid" style="margin-top:16px">
          <div><span class="n">강의장</span><h3>수용인원 120명</h3><p>공단 중심에 위치하며 지하철역 50m 근방으로 찾아오기 편리합니다. 쾌적하고 원활한 강의가 가능합니다.</p></div>
          <div><span class="n">실습장비</span><h3>동시 실습 100명</h3><p>현장에서 바로 적용 가능한 탐지 및 방재장비 실습으로, 실습 위주의 효과적이고 실용성 있는 교육을 제공합니다.</p></div>
          <div><span class="n">단체 신청</span><h3>대표아이디 관리</h3><p>대표아이디로 단체 교육 신청과 관리자 관리가 가능하며, 현장 경험이 풍부한 교수진이 강의합니다. 방문교육도 가능합니다.</p></div>
        </div>
      </div>

      <div class="callout" style="margin-top:30px">
        <h3>교육 신청 절차</h3>
        <p>교육시스템(edu.chemsafe.or.kr)에 접속하거나, 협회 홈페이지의 수강신청 배너를 통해 접수하실 수 있습니다.</p>
        <p style="margin-top:8px">※ 교육 신청 및 방문교육 문의 : <a href="tel:031-410-2992" style="font-weight:700">031-410-2992</a> (주말·야간교육 협의 가능)</p>
      </div>
      <div class="btnrow">
        <a class="btn btn--solid" href="https://edu.chemsafe.or.kr/" target="_blank" rel="noopener">수강신청 바로가기</a>
        <a class="btn btn--line" href="https://www.chemsafe.or.kr/training/safe.html" target="_blank" rel="noopener">협회 공식 안내 페이지</a>
      </div>
    </div>
  </section>

  <section class="sec sec--tint" id="osh">
    <div class="wrap">
      <div class="sec__head">
        {kick("산업안전보건 교육")}
        <h2>산업안전보건법에 따른<br>근로자 교육</h2>
      </div>
      <p class="law">산업안전보건법 제29조 (근로자에 대한 안전보건교육)</p>

      <div style="margin-top:26px">
        <h3 style="font-size:19px">교육 목적</h3>
        <ul class="bul" style="margin-top:12px">
          <li>근로자가 작업장의 안전보건에 관한 지식을 습득하고 대처능력을 배양하여 산업재해를 예방합니다.</li>
          <li>근로자의 생명과 신체 보호라는 인도적 측면과 함께 생산능률과 생산성 향상에 기여합니다.</li>
          <li>산업재해의 원인 및 경과 규명을 통해 인명과 재산을 재해로부터 보호합니다.</li>
          <li>질병의 원인과 예방 행동, 치료 행동의 방법 및 기술을 제공하여 자기건강관리 능력을 향상시킵니다.</li>
        </ul>
      </div>

      <div style="margin-top:30px">
        <h3 style="font-size:19px">정기교육 대상 및 시간</h3>
        <div class="tblwrap"><table>
          <thead><tr><th>교육과정</th><th>교육 대상</th><th>교육 시간</th></tr></thead>
          <tbody>
            <tr><td rowspan="4"><b>정기교육</b></td><td>사무직 종사 근로자</td><td>매분기 3시간 이상</td></tr>
            <tr><td>사무직 외 근로자 중 판매업무에 직접 종사하는 근로자</td><td>매분기 3시간 이상</td></tr>
            <tr><td>사무직 외 근로자 중 판매업무에 직접 종사하는 근로자 외의 근로자</td><td>매분기 6시간 이상</td></tr>
            <tr><td>관리감독자의 지위에 있는 사람</td><td>연간 16시간 이상</td></tr>
          </tbody>
        </table></div>
        <p class="tblnote">산업안전보건법(제26조 제1항) 별표4 정기교육 기준</p>
      </div>

      <div style="margin-top:34px">
        <h3 style="font-size:19px">관리감독자 안전보건교육</h3>
        <p style="margin-top:10px;font-size:16px;color:var(--ink-2);line-height:1.8">경영조직에서 생산과 관련되는 업무와 그 소속 직원을 직접 지휘·감독하는 부서의 장 또는 그 직위를 담당하는 자를 말합니다. 5인 이상 사업장에서는 사업주가 관리감독자를 지정하고, 관리감독자는 직무와 관련된 안전·보건 업무를 수행하여야 합니다.</p>
        <div class="tblwrap"><table>
          <tbody>
            <tr><th style="width:130px">교육 시간</th><td>연간 16시간 이상</td></tr>
            <tr><th>관련 법령</th><td>산업안전보건법 제16조(관리감독자), 제29조</td></tr>
            <tr><th>교육 대상</th><td>관리감독자의 지위에 있는 사람</td></tr>
          </tbody>
        </table></div>
      </div>

      <div style="margin-top:34px">
        <h3 style="font-size:19px">인터넷 원격교육</h3>
        <div class="grid" style="margin-top:16px">
          <div><span class="n">편의성</span><h3>시간과 장소의 자유</h3><p>업무에 지장을 초래하지 않고 특정 장소에 집합시킬 필요가 없는 교육 시스템입니다.</p></div>
          <div><span class="n">관리</span><h3>효과적인 교육관리</h3><p>학습지원 시스템으로 교육관리 정보가 제공되어 교육효과가 향상됩니다.</p></div>
          <div><span class="n">이수관리</span><h3>법정교육 이력 관리</h3><p>산업안전보건법 제31조·제32조에 의한 법정교육 이수 이력을 교육시스템에서 관리합니다.</p></div>
        </div>
        <h4 style="margin-top:24px;font-size:16px;font-weight:800;color:var(--brand-deep)">원격교육 과정</h4>
        <ul class="bul" style="margin-top:10px">
          <li>근로자 정기 안전보건교육</li>
          <li>관리감독자 교육</li>
          <li>기타 법정교육 — 성희롱예방, 개인정보보안, 장애인인식개선 교육 <span style="color:var(--steel)">(비환급)</span></li>
        </ul>
      </div>
      <div class="btnrow">
        <a class="btn btn--solid" href="https://edu.chemsafe.or.kr/" target="_blank" rel="noopener">수강신청 바로가기</a>
        <a class="btn btn--line" href="https://www.chemsafe.or.kr/training/safe_edu.html" target="_blank" rel="noopener">협회 공식 안내 페이지</a>
      </div>
    </div>
  </section>
''')

# ============================== ai-center.html ==============================
write("ai-center.html","AI특화 공동훈련센터",
"화학·환경·안전 분야 사업장의 규제 대응 업무를 AI 기반으로 전환하는 AX 교육. 국가인적자원개발컨소시엄 사업으로 협약 기업은 전액 무료로 지원받습니다.",
f'''  <section class="aikv netfx">
    <img class="aikv__hex" src="images/kv-hex.webp" alt="" aria-hidden="true">
    <div class="wrap aikv__in">
      <p class="bc">AI특화 공동훈련센터</p>
      <h1>규제 대응 업무의<br>AI 기반 전환을 지원합니다</h1>
      <p>화학·환경·안전 분야 사업장을 대상으로 AX 기반 현장 맞춤형 교육을 지원합니다. 단순 강의에 그치지 않고 진단에서 확산까지 네 단계로 운영합니다.</p>
    </div>
  </section>

  <section class="sec sec--brand netfx">
    <img class="phero__mark" src="images/mark-white.svg" alt="" aria-hidden="true">
    <div class="wrap" style="position:relative;z-index:1">
      <div class="sec__head">
        <p class="kicker"><img src="images/mark-light.svg" alt="">운영 방식</p>
        <h2>진단에서 확산까지<br>네 단계</h2>
      </div>
      <ol class="pipe">
        <li><span class="n">01</span><div><h3>진단</h3><p>사업장의 업무 흐름과 데이터 관리 현황을 진단하여 AI 적용이 가능한 업무를 도출합니다.</p></div></li>
        <li><span class="n">02</span><div><h3>교육</h3><p>화학·안전·환경 직무별 과정을 통해 담당자가 직접 활용할 수 있는 수준까지 교육합니다.</p></div></li>
        <li><span class="n">03</span><div><h3>현장적용</h3><p>교육 내용을 점검·기록·보고 등 실제 업무에 적용하도록 코칭을 제공합니다.</p></div></li>
        <li><span class="n">04</span><div><h3>확산</h3><p>개별 담당자의 활용 방식을 조직의 관리체계로 정착시키고 확산합니다.</p></div></li>
      </ol>
      <div class="free">
        <h3>진단부터 교육 · 코칭까지 전액 무료 지원</h3>
        <p>국가인적자원개발컨소시엄 사업으로 운영되어 협약 기업은 별도의 비용을 부담하지 않습니다. 교육 신청자는 고용보험에 가입되어 있어야 합니다.</p>
      </div>
      <div class="stats">
        <div><b>61개사</b><span>협약 기업</span></div>
        <div><b>4.8 / 5.0</b><span>교육 만족도</span></div>
        <div><b>2 · 4시간</b><span>과정별 편성 시간</span></div>
      </div>
    </div>
  </section>

  <section class="sec" id="courses">
    <div class="wrap">
      <div class="sec__head">
        {kick("교육과정")}
        <h2>직무별 여섯 개 과정</h2>
        <p class="sec__sub measure">과정명을 선택하시면 세부 차시와 교육 시간, 정원을 확인하실 수 있습니다.</p>
      </div>
      <details class="acc" open>
        <summary><span class="tag">화학 · 일반</span><div class="ttl">화학물질 규제 대응을 위한 데이터 기반 스마트 화학안전(AX) 실무</div></summary>
        <div class="acc__body"><div class="tblwrap"><table><thead><tr><th>차시</th><th>시간 · 정원</th></tr></thead><tbody>
          <tr><td>화학안전관리 AX 전환 사례 이해</td><td>2시간 · 20명</td></tr>
          <tr><td>화학안전 규제 대응을 위한 데이터 기반 관리체계 구축</td><td>4시간 · 20명</td></tr></tbody></table></div></div>
      </details>
      <details class="acc">
        <summary><span class="tag">화학 · 일반</span><div class="ttl">AX 기반 취급시설 리스크 진단 및 스마트 점검체계 구축</div></summary>
        <div class="acc__body"><div class="tblwrap"><table><thead><tr><th>차시</th><th>시간 · 정원</th></tr></thead><tbody>
          <tr><td>산업안전·보건 관리 업무 AX 이해 및 활용 입문</td><td>2시간 · 20명</td></tr>
          <tr><td>취급시설 리스크 관리와 데이터 기반 점검체계 설계</td><td>4시간 · 20명</td></tr></tbody></table></div></div>
      </details>
      <details class="acc">
        <summary><span class="tag">안전 · 전문</span><div class="ttl">중대재해 제로(Zero)를 위한 산업안전 AX 관리체계 마스터</div></summary>
        <div class="acc__body"><div class="tblwrap"><table><thead><tr><th>차시</th><th>시간 · 정원</th></tr></thead><tbody>
          <tr><td>산업안전·보건 관리 업무 AX 이해 및 활용 입문</td><td>2시간 · 20명</td></tr>
          <tr><td>산업안전·중대재해 대응 AX 기반 관리체계 입문</td><td>4시간 · 20명</td></tr></tbody></table></div></div>
      </details>
      <details class="acc">
        <summary><span class="tag">안전 · 전문</span><div class="ttl">생성형 AI 활용 위험성평가 자동화 및 현장 개선 실무</div></summary>
        <div class="acc__body"><div class="tblwrap"><table><thead><tr><th>차시</th><th>시간 · 정원</th></tr></thead><tbody>
          <tr><td>산업안전·보건 관리 업무 AX 이해 및 활용 입문</td><td>2시간 · 20명</td></tr>
          <tr><td>AI 활용 위험성평가 자동화 및 개선조치 실무</td><td>4시간 · 20명</td></tr></tbody></table></div></div>
      </details>
      <details class="acc">
        <summary><span class="tag">환경 · 전문</span><div class="ttl">데이터 기반의 환경 컴플라이언스 선제적 대응 및 리스크 관리</div></summary>
        <div class="acc__body"><div class="tblwrap"><table><thead><tr><th>차시</th><th>시간 · 정원</th></tr></thead><tbody>
          <tr><td>환경관리 AX 전환 사례 이해</td><td>2시간 · 20명</td></tr>
          <tr><td>취급시설 리스크 관리와 데이터 기반 점검체계 설계</td><td>4시간 · 20명</td></tr></tbody></table></div></div>
      </details>
      <details class="acc">
        <summary><span class="tag">화학 · 전문</span><div class="ttl">PSM 12대 요소 실무 적용</div></summary>
        <div class="acc__body"><p style="font-size:15.5px;color:var(--steel)">세부 차시는 훈련센터 교육과정 페이지에서 확인하실 수 있습니다.</p></div>
      </details>
      <div class="btnrow"><a class="btn btn--line" href="https://ai.chemsafe.or.kr/class/class_schedule.html" target="_blank" rel="noopener">연간 교육 일정 확인</a></div>
    </div>
  </section>

  <section class="sec sec--tint" id="howto">
    <div class="wrap">
      <div class="sec__head">
        {kick("참여 절차")}
        <h2>협약 신청부터 수료까지</h2>
      </div>
      <ol class="steps">
        <li><h3>협약 신청</h3><p>협약 신청서에 직인을 날인하여 등록합니다. 등록 후 협약 기업 조회가 가능합니다.</p></li>
        <li><h3>회원 가입</h3><p>협약 기업을 조회하여 소속을 선택합니다. 조회되지 않는 경우 '소속 협약기업 없음'으로 가입한 후 등록하실 수 있습니다.</p></li>
        <li><h3>수강신청</h3><p>교육 일정과 상세 내용을 확인한 후 신청합니다.</p></li>
        <li><h3>수강 확정</h3><p>확정 시 SMS로 안내합니다. 정원 초과 시 대기자로 접수되며, 결원 발생 순서에 따라 안내드립니다.</p></li>
        <li><h3>과정 수강</h3><p>출석 관리 앱(APP)을 설치한 후 수강합니다.</p></li>
        <li><h3>과정 수료</h3><p>수료 후 수료증을 발급받으실 수 있습니다.</p></li>
      </ol>
      <div class="callout">
        <h3>신청 전 확인 사항</h3>
        <ul class="bul" style="margin-top:12px">
          <li>교육 신청자는 고용보험에 가입되어 있어야 합니다.</li>
          <li>교육 취소는 교육 시작 7일 전까지 가능하며, 이후 취소하거나 참석하지 않는 경우 불이익이 있을 수 있습니다.</li>
          <li>부득이하게 참석이 어려운 경우 사전에 고객센터로 연락 주시기 바랍니다.</li>
        </ul>
      </div>
      <ul class="dl">
        <li><span class="k">교육 문의</span><span class="v"><a href="tel:031-410-2992">031-410-2992</a> · 평일 10:00~17:00 (점심 12:00~13:00)</span></li>
        <li><span class="k">이메일</span><span class="v"><a href="mailto:chem.edu@chemsafe.or.kr">chem.edu@chemsafe.or.kr</a></span></li>
        <li><span class="k">온라인 문의</span><span class="v"><a href="https://ai.chemsafe.or.kr/cscenter/inquiry.html" target="_blank" rel="noopener">훈련센터 문의하기</a></span></li>
      </ul>
      <div class="btnrow"><a class="btn btn--solid" href="https://ai.chemsafe.or.kr/" target="_blank" rel="noopener">AI특화 공동훈련센터 바로가기</a></div>
    </div>
  </section>
''')

# ============================== member.html ==============================
write("member.html","회원 안내",
"한국화학안전협회 회원 사업장에 제공하는 화학안전 정보 서비스, 업무 대행 및 위탁, 안전교육 지원 내용을 안내합니다.",
phero("회원관리","회원 사업장에<br>제공하는 것","정보 제공부터 법정 업무 대행, 맞춤형 안전교육까지 지원합니다.") + f'''
  <section class="sec" id="info">
    <div class="wrap">
      <div class="sec__head">
        {kick("정보제공")}
        <h2>화학안전 정보와<br>자료를 제공합니다</h2>
      </div>
      <div class="prose measure">
        <p>화학물질 취급 관련 사업장의 안전관리에 대한 각종 정보 및 자료를 제공합니다. 또한 해외 화학안전 전문기관과의 협업을 통하여 다양한 화학안전 기술을 도입하고 정보를 공유하고 있습니다.</p>
        <p>세미나, 홍보, 우수 안전 사업장 해외 견학 등의 다양한 프로그램을 통하여 회원들의 안전관리 능력을 배양하고자 합니다.</p>
      </div>
    </div>
  </section>

  <section class="sec sec--tint" id="agency">
    <div class="wrap">
      <div class="sec__head">
        {kick("업무대행 및 위탁")}
        <h2>법정 업무를<br>대신 처리합니다</h2>
      </div>
      <ul class="bul">
        <li>MSDS 작성 대행 및 컨설팅 업무 지원</li>
        <li>PSM(공정안전보고서) 작성 대행</li>
        <li>화학물질 확인 및 시설 자체점검 대행과 컨설팅</li>
        <li>화학사고예방관리계획서 작성 컨설팅</li>
        <li>화평법에 의한 화학물질 보고, 등록, 신고 의무 대행</li>
        <li>기타 사업장 안전관리에 관한 사항</li>
      </ul>
      <div class="btnrow">
        <a class="btn btn--line" href="business.html">협회 주요 사업 보기</a>
        <a class="btn btn--line" href="https://www.chemsafe.or.kr/member/service.html" target="_blank" rel="noopener">협회 공식 안내 페이지</a>
      </div>
    </div>
  </section>

  <section class="sec" id="support">
    <div class="wrap">
      <div class="sec__head">
        {kick("안전교육지원")}
        <h2>대상에 맞춘<br>교육을 제공합니다</h2>
      </div>
      <ul class="bul">
        <li>유해화학물질 취급자에 대한 사고 예방 교육</li>
        <li>유해화학물질 사고 발생 시 최소한의 대응 조치 방법과 절차 교육</li>
        <li>교육 대상별 맞춤형 교육 확대 (취급자, 관리자, 학생, 일반인, 어린이 등)</li>
        <li>화관법 개정과 화평법 제정에 따른 전문가 양성 및 실무 책임 교육 실시</li>
        <li>세분화된 교육과정의 차별화를 통해 기술 인력의 전문성과 대비 능력 배양</li>
        <li>해외 전문 교육 강사 초빙을 통한 해외 취급 관리 기술 습득</li>
      </ul>
      <div class="btnrow">
        <a class="btn btn--line" href="education.html">안전교육 보기</a>
        <a class="btn btn--line" href="https://www.chemsafe.or.kr/member/training.html" target="_blank" rel="noopener">협회 공식 안내 페이지</a>
      </div>
    </div>
  </section>

  <section class="sec sec--soft" id="join">
    <div class="wrap">
      <div class="sec__head">
        {kick("회원가입")}
        <h2>가입 안내</h2>
        <p class="sec__sub measure">회원가입은 협회 공식 홈페이지의 회원관리 메뉴에서 신청하실 수 있습니다. 절차나 회비에 대한 문의는 전화로 안내드립니다.</p>
      </div>
      <div class="btnrow">
        <a class="btn btn--solid" href="https://www.chemsafe.or.kr/member/join.html" target="_blank" rel="noopener">회원가입 신청</a>
        <a class="btn btn--line" href="tel:1644-9049">전화 문의 1644-9049</a>
      </div>
    </div>
  </section>
''')

# ============================== contact.html ==============================
write("contact.html","오시는 길 · 문의",
"한국화학안전협회 본회와 교육장 위치, 연락처 및 상담 시간을 안내합니다. 경기도 안산시 단원구.",
phero("찾아오시는 길","안산에 있습니다","본회와 교육장이 각각 다른 위치에 있으니 방문 전 확인해 주시기 바랍니다.") + f'''
  <section class="sec">
    <div class="wrap">
      <div class="places">
        <div class="place">
          <h3>본회</h3>
          <p class="addr">경기도 안산시 단원구 고잔1길 76<br>리치프라자 401~2호</p>
          <p class="sub">(고잔동 540-9)</p>
          <a class="map" href="https://map.naver.com/p/search/경기도 안산시 단원구 고잔1길 76" target="_blank" rel="noopener">네이버 지도에서 보기</a>
        </div>
        <div class="place">
          <h3>교육장</h3>
          <p class="addr">경기도 안산시 단원구 동산로 63, 3층<br>기업은행 반월지점 건물</p>
          <p class="sub">(원시동 773-9) · 지하철역 50m 근방, 수용인원 120명</p>
          <a class="map" href="https://map.naver.com/p/search/경기도 안산시 단원구 동산로 63" target="_blank" rel="noopener">네이버 지도에서 보기</a>
        </div>
      </div>
      <ul class="dl" style="margin-top:0">
        <li><span class="k">대표전화</span><span class="v"><a href="tel:1644-9049">1644-9049</a> (代) · <a href="tel:031-410-2991">031-410-2991~2</a></span></li>
        <li><span class="k">팩스</span><span class="v">031-410-2994</span></li>
        <li><span class="k">교육 문의</span><span class="v"><a href="tel:031-410-2992">031-410-2992</a> · 주말·야간교육 협의 가능</span></li>
        <li><span class="k">이메일</span><span class="v"><a href="mailto:chem.edu@chemsafe.or.kr">chem.edu@chemsafe.or.kr</a></span></li>
        <li><span class="k">상담시간</span><span class="v">평일 09:00 ~ 18:00 (토·일요일 및 공휴일 휴무)</span></li>
      </ul>
      <div class="btnrow">
        <a class="btn btn--solid" href="tel:1644-9049">전화 걸기</a>
        <a class="btn btn--line" href="https://www.chemsafe.or.kr/prcenter/qna.html" target="_blank" rel="noopener">온라인 문의</a>
      </div>
    </div>
  </section>
''')
