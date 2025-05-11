// Generated from /Users/lg/antlr/LittleDuckParser.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class LittleDuckParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		PROGRAM=1, MAIN=2, END=3, VAR=4, INT=5, FLOAT=6, VOID=7, IF=8, ELSE=9, 
		WHILE=10, DO=11, PRINT=12, ID=13, CTE_INT=14, CTE_FLOAT=15, CTE_STRING=16, 
		PLUS=17, MINUS=18, MULT=19, DIV=20, EQUAL=21, NEQ=22, LT=23, GT=24, LPAREN=25, 
		RPAREN=26, LBRACE=27, RBRACE=28, SEMICOLON=29, COMMA=30, COLON=31, LINE_COMMENT=32, 
		WS=33;
	public static final int
		RULE_programa = 0, RULE_vars = 1, RULE_var_decl = 2, RULE_tipo = 3, RULE_bloque = 4, 
		RULE_estatuto = 5, RULE_asignacion = 6, RULE_condicion = 7, RULE_ciclo = 8, 
		RULE_escritura = 9, RULE_expresion = 10, RULE_exp = 11, RULE_termino = 12, 
		RULE_factor = 13, RULE_var_cte = 14;
	private static String[] makeRuleNames() {
		return new String[] {
			"programa", "vars", "var_decl", "tipo", "bloque", "estatuto", "asignacion", 
			"condicion", "ciclo", "escritura", "expresion", "exp", "termino", "factor", 
			"var_cte"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'program'", "'main'", "'end'", "'var'", "'int'", "'float'", "'void'", 
			"'if'", "'else'", "'while'", "'do'", "'print'", null, null, null, null, 
			"'+'", "'-'", "'*'", "'/'", "'='", "'!='", "'<'", "'>'", "'('", "')'", 
			"'{'", "'}'", "';'", "','", "':'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "PROGRAM", "MAIN", "END", "VAR", "INT", "FLOAT", "VOID", "IF", 
			"ELSE", "WHILE", "DO", "PRINT", "ID", "CTE_INT", "CTE_FLOAT", "CTE_STRING", 
			"PLUS", "MINUS", "MULT", "DIV", "EQUAL", "NEQ", "LT", "GT", "LPAREN", 
			"RPAREN", "LBRACE", "RBRACE", "SEMICOLON", "COMMA", "COLON", "LINE_COMMENT", 
			"WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "LittleDuckParser.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public LittleDuckParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramaContext extends ParserRuleContext {
		public TerminalNode PROGRAM() { return getToken(LittleDuckParser.PROGRAM, 0); }
		public TerminalNode ID() { return getToken(LittleDuckParser.ID, 0); }
		public TerminalNode SEMICOLON() { return getToken(LittleDuckParser.SEMICOLON, 0); }
		public VarsContext vars() {
			return getRuleContext(VarsContext.class,0);
		}
		public BloqueContext bloque() {
			return getRuleContext(BloqueContext.class,0);
		}
		public TerminalNode END() { return getToken(LittleDuckParser.END, 0); }
		public ProgramaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_programa; }
	}

	public final ProgramaContext programa() throws RecognitionException {
		ProgramaContext _localctx = new ProgramaContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_programa);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(30);
			match(PROGRAM);
			setState(31);
			match(ID);
			setState(32);
			match(SEMICOLON);
			setState(33);
			vars();
			setState(34);
			bloque();
			setState(35);
			match(END);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class VarsContext extends ParserRuleContext {
		public TerminalNode VAR() { return getToken(LittleDuckParser.VAR, 0); }
		public List<Var_declContext> var_decl() {
			return getRuleContexts(Var_declContext.class);
		}
		public Var_declContext var_decl(int i) {
			return getRuleContext(Var_declContext.class,i);
		}
		public VarsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_vars; }
	}

	public final VarsContext vars() throws RecognitionException {
		VarsContext _localctx = new VarsContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_vars);
		int _la;
		try {
			setState(44);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case VAR:
				enterOuterAlt(_localctx, 1);
				{
				setState(37);
				match(VAR);
				setState(39); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(38);
					var_decl();
					}
					}
					setState(41); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( _la==ID );
				}
				break;
			case LBRACE:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Var_declContext extends ParserRuleContext {
		public List<TerminalNode> ID() { return getTokens(LittleDuckParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(LittleDuckParser.ID, i);
		}
		public TerminalNode COLON() { return getToken(LittleDuckParser.COLON, 0); }
		public TipoContext tipo() {
			return getRuleContext(TipoContext.class,0);
		}
		public TerminalNode SEMICOLON() { return getToken(LittleDuckParser.SEMICOLON, 0); }
		public List<TerminalNode> COMMA() { return getTokens(LittleDuckParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(LittleDuckParser.COMMA, i);
		}
		public Var_declContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_var_decl; }
	}

	public final Var_declContext var_decl() throws RecognitionException {
		Var_declContext _localctx = new Var_declContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_var_decl);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(46);
			match(ID);
			setState(51);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(47);
				match(COMMA);
				setState(48);
				match(ID);
				}
				}
				setState(53);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(54);
			match(COLON);
			setState(55);
			tipo();
			setState(56);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TipoContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(LittleDuckParser.INT, 0); }
		public TerminalNode FLOAT() { return getToken(LittleDuckParser.FLOAT, 0); }
		public TipoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tipo; }
	}

	public final TipoContext tipo() throws RecognitionException {
		TipoContext _localctx = new TipoContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_tipo);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(58);
			_la = _input.LA(1);
			if ( !(_la==INT || _la==FLOAT) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BloqueContext extends ParserRuleContext {
		public TerminalNode LBRACE() { return getToken(LittleDuckParser.LBRACE, 0); }
		public TerminalNode RBRACE() { return getToken(LittleDuckParser.RBRACE, 0); }
		public List<EstatutoContext> estatuto() {
			return getRuleContexts(EstatutoContext.class);
		}
		public EstatutoContext estatuto(int i) {
			return getRuleContext(EstatutoContext.class,i);
		}
		public BloqueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bloque; }
	}

	public final BloqueContext bloque() throws RecognitionException {
		BloqueContext _localctx = new BloqueContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_bloque);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(60);
			match(LBRACE);
			setState(64);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 13568L) != 0)) {
				{
				{
				setState(61);
				estatuto();
				}
				}
				setState(66);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(67);
			match(RBRACE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class EstatutoContext extends ParserRuleContext {
		public AsignacionContext asignacion() {
			return getRuleContext(AsignacionContext.class,0);
		}
		public CondicionContext condicion() {
			return getRuleContext(CondicionContext.class,0);
		}
		public CicloContext ciclo() {
			return getRuleContext(CicloContext.class,0);
		}
		public EscrituraContext escritura() {
			return getRuleContext(EscrituraContext.class,0);
		}
		public EstatutoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_estatuto; }
	}

	public final EstatutoContext estatuto() throws RecognitionException {
		EstatutoContext _localctx = new EstatutoContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_estatuto);
		try {
			setState(73);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(69);
				asignacion();
				}
				break;
			case IF:
				enterOuterAlt(_localctx, 2);
				{
				setState(70);
				condicion();
				}
				break;
			case WHILE:
				enterOuterAlt(_localctx, 3);
				{
				setState(71);
				ciclo();
				}
				break;
			case PRINT:
				enterOuterAlt(_localctx, 4);
				{
				setState(72);
				escritura();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AsignacionContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(LittleDuckParser.ID, 0); }
		public TerminalNode EQUAL() { return getToken(LittleDuckParser.EQUAL, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public TerminalNode SEMICOLON() { return getToken(LittleDuckParser.SEMICOLON, 0); }
		public AsignacionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_asignacion; }
	}

	public final AsignacionContext asignacion() throws RecognitionException {
		AsignacionContext _localctx = new AsignacionContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_asignacion);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(75);
			match(ID);
			setState(76);
			match(EQUAL);
			setState(77);
			expresion();
			setState(78);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CondicionContext extends ParserRuleContext {
		public TerminalNode IF() { return getToken(LittleDuckParser.IF, 0); }
		public TerminalNode LPAREN() { return getToken(LittleDuckParser.LPAREN, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(LittleDuckParser.RPAREN, 0); }
		public List<BloqueContext> bloque() {
			return getRuleContexts(BloqueContext.class);
		}
		public BloqueContext bloque(int i) {
			return getRuleContext(BloqueContext.class,i);
		}
		public TerminalNode ELSE() { return getToken(LittleDuckParser.ELSE, 0); }
		public CondicionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condicion; }
	}

	public final CondicionContext condicion() throws RecognitionException {
		CondicionContext _localctx = new CondicionContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_condicion);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(80);
			match(IF);
			setState(81);
			match(LPAREN);
			setState(82);
			expresion();
			setState(83);
			match(RPAREN);
			setState(84);
			bloque();
			setState(87);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ELSE) {
				{
				setState(85);
				match(ELSE);
				setState(86);
				bloque();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CicloContext extends ParserRuleContext {
		public TerminalNode WHILE() { return getToken(LittleDuckParser.WHILE, 0); }
		public TerminalNode LPAREN() { return getToken(LittleDuckParser.LPAREN, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(LittleDuckParser.RPAREN, 0); }
		public BloqueContext bloque() {
			return getRuleContext(BloqueContext.class,0);
		}
		public CicloContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ciclo; }
	}

	public final CicloContext ciclo() throws RecognitionException {
		CicloContext _localctx = new CicloContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_ciclo);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(89);
			match(WHILE);
			setState(90);
			match(LPAREN);
			setState(91);
			expresion();
			setState(92);
			match(RPAREN);
			setState(93);
			bloque();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class EscrituraContext extends ParserRuleContext {
		public TerminalNode PRINT() { return getToken(LittleDuckParser.PRINT, 0); }
		public TerminalNode LPAREN() { return getToken(LittleDuckParser.LPAREN, 0); }
		public TerminalNode RPAREN() { return getToken(LittleDuckParser.RPAREN, 0); }
		public TerminalNode SEMICOLON() { return getToken(LittleDuckParser.SEMICOLON, 0); }
		public List<ExpresionContext> expresion() {
			return getRuleContexts(ExpresionContext.class);
		}
		public ExpresionContext expresion(int i) {
			return getRuleContext(ExpresionContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(LittleDuckParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(LittleDuckParser.COMMA, i);
		}
		public EscrituraContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_escritura; }
	}

	public final EscrituraContext escritura() throws RecognitionException {
		EscrituraContext _localctx = new EscrituraContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_escritura);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(95);
			match(PRINT);
			setState(96);
			match(LPAREN);
			setState(105);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 34070528L) != 0)) {
				{
				setState(97);
				expresion();
				setState(102);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(98);
					match(COMMA);
					setState(99);
					expresion();
					}
					}
					setState(104);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(107);
			match(RPAREN);
			setState(108);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpresionContext extends ParserRuleContext {
		public List<ExpContext> exp() {
			return getRuleContexts(ExpContext.class);
		}
		public ExpContext exp(int i) {
			return getRuleContext(ExpContext.class,i);
		}
		public TerminalNode LT() { return getToken(LittleDuckParser.LT, 0); }
		public TerminalNode GT() { return getToken(LittleDuckParser.GT, 0); }
		public TerminalNode EQUAL() { return getToken(LittleDuckParser.EQUAL, 0); }
		public TerminalNode NEQ() { return getToken(LittleDuckParser.NEQ, 0); }
		public ExpresionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expresion; }
	}

	public final ExpresionContext expresion() throws RecognitionException {
		ExpresionContext _localctx = new ExpresionContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_expresion);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(110);
			exp();
			setState(113);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 31457280L) != 0)) {
				{
				setState(111);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 31457280L) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(112);
				exp();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpContext extends ParserRuleContext {
		public List<TerminoContext> termino() {
			return getRuleContexts(TerminoContext.class);
		}
		public TerminoContext termino(int i) {
			return getRuleContext(TerminoContext.class,i);
		}
		public List<TerminalNode> PLUS() { return getTokens(LittleDuckParser.PLUS); }
		public TerminalNode PLUS(int i) {
			return getToken(LittleDuckParser.PLUS, i);
		}
		public List<TerminalNode> MINUS() { return getTokens(LittleDuckParser.MINUS); }
		public TerminalNode MINUS(int i) {
			return getToken(LittleDuckParser.MINUS, i);
		}
		public ExpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp; }
	}

	public final ExpContext exp() throws RecognitionException {
		ExpContext _localctx = new ExpContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_exp);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(115);
			termino();
			setState(120);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==PLUS || _la==MINUS) {
				{
				{
				setState(116);
				_la = _input.LA(1);
				if ( !(_la==PLUS || _la==MINUS) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(117);
				termino();
				}
				}
				setState(122);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TerminoContext extends ParserRuleContext {
		public List<FactorContext> factor() {
			return getRuleContexts(FactorContext.class);
		}
		public FactorContext factor(int i) {
			return getRuleContext(FactorContext.class,i);
		}
		public List<TerminalNode> MULT() { return getTokens(LittleDuckParser.MULT); }
		public TerminalNode MULT(int i) {
			return getToken(LittleDuckParser.MULT, i);
		}
		public List<TerminalNode> DIV() { return getTokens(LittleDuckParser.DIV); }
		public TerminalNode DIV(int i) {
			return getToken(LittleDuckParser.DIV, i);
		}
		public TerminoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_termino; }
	}

	public final TerminoContext termino() throws RecognitionException {
		TerminoContext _localctx = new TerminoContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_termino);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(123);
			factor();
			setState(128);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==MULT || _la==DIV) {
				{
				{
				setState(124);
				_la = _input.LA(1);
				if ( !(_la==MULT || _la==DIV) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(125);
				factor();
				}
				}
				setState(130);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FactorContext extends ParserRuleContext {
		public TerminalNode LPAREN() { return getToken(LittleDuckParser.LPAREN, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(LittleDuckParser.RPAREN, 0); }
		public TerminalNode PLUS() { return getToken(LittleDuckParser.PLUS, 0); }
		public FactorContext factor() {
			return getRuleContext(FactorContext.class,0);
		}
		public TerminalNode MINUS() { return getToken(LittleDuckParser.MINUS, 0); }
		public Var_cteContext var_cte() {
			return getRuleContext(Var_cteContext.class,0);
		}
		public FactorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_factor; }
	}

	public final FactorContext factor() throws RecognitionException {
		FactorContext _localctx = new FactorContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_factor);
		try {
			setState(140);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LPAREN:
				enterOuterAlt(_localctx, 1);
				{
				setState(131);
				match(LPAREN);
				setState(132);
				expresion();
				setState(133);
				match(RPAREN);
				}
				break;
			case PLUS:
				enterOuterAlt(_localctx, 2);
				{
				setState(135);
				match(PLUS);
				setState(136);
				factor();
				}
				break;
			case MINUS:
				enterOuterAlt(_localctx, 3);
				{
				setState(137);
				match(MINUS);
				setState(138);
				factor();
				}
				break;
			case ID:
			case CTE_INT:
			case CTE_FLOAT:
			case CTE_STRING:
				enterOuterAlt(_localctx, 4);
				{
				setState(139);
				var_cte();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Var_cteContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(LittleDuckParser.ID, 0); }
		public TerminalNode CTE_INT() { return getToken(LittleDuckParser.CTE_INT, 0); }
		public TerminalNode CTE_FLOAT() { return getToken(LittleDuckParser.CTE_FLOAT, 0); }
		public TerminalNode CTE_STRING() { return getToken(LittleDuckParser.CTE_STRING, 0); }
		public Var_cteContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_var_cte; }
	}

	public final Var_cteContext var_cte() throws RecognitionException {
		Var_cteContext _localctx = new Var_cteContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_var_cte);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(142);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 122880L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001!\u0091\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0001"+
		"\u0001\u0001\u0004\u0001(\b\u0001\u000b\u0001\f\u0001)\u0001\u0001\u0003"+
		"\u0001-\b\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0005\u00022\b\u0002"+
		"\n\u0002\f\u00025\t\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0005\u0004?\b\u0004"+
		"\n\u0004\f\u0004B\t\u0004\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0003\u0005J\b\u0005\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0003\u0007X\b\u0007"+
		"\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\t\u0001\t\u0001"+
		"\t\u0001\t\u0001\t\u0005\te\b\t\n\t\f\th\t\t\u0003\tj\b\t\u0001\t\u0001"+
		"\t\u0001\t\u0001\n\u0001\n\u0001\n\u0003\nr\b\n\u0001\u000b\u0001\u000b"+
		"\u0001\u000b\u0005\u000bw\b\u000b\n\u000b\f\u000bz\t\u000b\u0001\f\u0001"+
		"\f\u0001\f\u0005\f\u007f\b\f\n\f\f\f\u0082\t\f\u0001\r\u0001\r\u0001\r"+
		"\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0003\r\u008d\b\r\u0001"+
		"\u000e\u0001\u000e\u0001\u000e\u0000\u0000\u000f\u0000\u0002\u0004\u0006"+
		"\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018\u001a\u001c\u0000\u0005\u0001"+
		"\u0000\u0005\u0006\u0001\u0000\u0015\u0018\u0001\u0000\u0011\u0012\u0001"+
		"\u0000\u0013\u0014\u0001\u0000\r\u0010\u0091\u0000\u001e\u0001\u0000\u0000"+
		"\u0000\u0002,\u0001\u0000\u0000\u0000\u0004.\u0001\u0000\u0000\u0000\u0006"+
		":\u0001\u0000\u0000\u0000\b<\u0001\u0000\u0000\u0000\nI\u0001\u0000\u0000"+
		"\u0000\fK\u0001\u0000\u0000\u0000\u000eP\u0001\u0000\u0000\u0000\u0010"+
		"Y\u0001\u0000\u0000\u0000\u0012_\u0001\u0000\u0000\u0000\u0014n\u0001"+
		"\u0000\u0000\u0000\u0016s\u0001\u0000\u0000\u0000\u0018{\u0001\u0000\u0000"+
		"\u0000\u001a\u008c\u0001\u0000\u0000\u0000\u001c\u008e\u0001\u0000\u0000"+
		"\u0000\u001e\u001f\u0005\u0001\u0000\u0000\u001f \u0005\r\u0000\u0000"+
		" !\u0005\u001d\u0000\u0000!\"\u0003\u0002\u0001\u0000\"#\u0003\b\u0004"+
		"\u0000#$\u0005\u0003\u0000\u0000$\u0001\u0001\u0000\u0000\u0000%\'\u0005"+
		"\u0004\u0000\u0000&(\u0003\u0004\u0002\u0000\'&\u0001\u0000\u0000\u0000"+
		"()\u0001\u0000\u0000\u0000)\'\u0001\u0000\u0000\u0000)*\u0001\u0000\u0000"+
		"\u0000*-\u0001\u0000\u0000\u0000+-\u0001\u0000\u0000\u0000,%\u0001\u0000"+
		"\u0000\u0000,+\u0001\u0000\u0000\u0000-\u0003\u0001\u0000\u0000\u0000"+
		".3\u0005\r\u0000\u0000/0\u0005\u001e\u0000\u000002\u0005\r\u0000\u0000"+
		"1/\u0001\u0000\u0000\u000025\u0001\u0000\u0000\u000031\u0001\u0000\u0000"+
		"\u000034\u0001\u0000\u0000\u000046\u0001\u0000\u0000\u000053\u0001\u0000"+
		"\u0000\u000067\u0005\u001f\u0000\u000078\u0003\u0006\u0003\u000089\u0005"+
		"\u001d\u0000\u00009\u0005\u0001\u0000\u0000\u0000:;\u0007\u0000\u0000"+
		"\u0000;\u0007\u0001\u0000\u0000\u0000<@\u0005\u001b\u0000\u0000=?\u0003"+
		"\n\u0005\u0000>=\u0001\u0000\u0000\u0000?B\u0001\u0000\u0000\u0000@>\u0001"+
		"\u0000\u0000\u0000@A\u0001\u0000\u0000\u0000AC\u0001\u0000\u0000\u0000"+
		"B@\u0001\u0000\u0000\u0000CD\u0005\u001c\u0000\u0000D\t\u0001\u0000\u0000"+
		"\u0000EJ\u0003\f\u0006\u0000FJ\u0003\u000e\u0007\u0000GJ\u0003\u0010\b"+
		"\u0000HJ\u0003\u0012\t\u0000IE\u0001\u0000\u0000\u0000IF\u0001\u0000\u0000"+
		"\u0000IG\u0001\u0000\u0000\u0000IH\u0001\u0000\u0000\u0000J\u000b\u0001"+
		"\u0000\u0000\u0000KL\u0005\r\u0000\u0000LM\u0005\u0015\u0000\u0000MN\u0003"+
		"\u0014\n\u0000NO\u0005\u001d\u0000\u0000O\r\u0001\u0000\u0000\u0000PQ"+
		"\u0005\b\u0000\u0000QR\u0005\u0019\u0000\u0000RS\u0003\u0014\n\u0000S"+
		"T\u0005\u001a\u0000\u0000TW\u0003\b\u0004\u0000UV\u0005\t\u0000\u0000"+
		"VX\u0003\b\u0004\u0000WU\u0001\u0000\u0000\u0000WX\u0001\u0000\u0000\u0000"+
		"X\u000f\u0001\u0000\u0000\u0000YZ\u0005\n\u0000\u0000Z[\u0005\u0019\u0000"+
		"\u0000[\\\u0003\u0014\n\u0000\\]\u0005\u001a\u0000\u0000]^\u0003\b\u0004"+
		"\u0000^\u0011\u0001\u0000\u0000\u0000_`\u0005\f\u0000\u0000`i\u0005\u0019"+
		"\u0000\u0000af\u0003\u0014\n\u0000bc\u0005\u001e\u0000\u0000ce\u0003\u0014"+
		"\n\u0000db\u0001\u0000\u0000\u0000eh\u0001\u0000\u0000\u0000fd\u0001\u0000"+
		"\u0000\u0000fg\u0001\u0000\u0000\u0000gj\u0001\u0000\u0000\u0000hf\u0001"+
		"\u0000\u0000\u0000ia\u0001\u0000\u0000\u0000ij\u0001\u0000\u0000\u0000"+
		"jk\u0001\u0000\u0000\u0000kl\u0005\u001a\u0000\u0000lm\u0005\u001d\u0000"+
		"\u0000m\u0013\u0001\u0000\u0000\u0000nq\u0003\u0016\u000b\u0000op\u0007"+
		"\u0001\u0000\u0000pr\u0003\u0016\u000b\u0000qo\u0001\u0000\u0000\u0000"+
		"qr\u0001\u0000\u0000\u0000r\u0015\u0001\u0000\u0000\u0000sx\u0003\u0018"+
		"\f\u0000tu\u0007\u0002\u0000\u0000uw\u0003\u0018\f\u0000vt\u0001\u0000"+
		"\u0000\u0000wz\u0001\u0000\u0000\u0000xv\u0001\u0000\u0000\u0000xy\u0001"+
		"\u0000\u0000\u0000y\u0017\u0001\u0000\u0000\u0000zx\u0001\u0000\u0000"+
		"\u0000{\u0080\u0003\u001a\r\u0000|}\u0007\u0003\u0000\u0000}\u007f\u0003"+
		"\u001a\r\u0000~|\u0001\u0000\u0000\u0000\u007f\u0082\u0001\u0000\u0000"+
		"\u0000\u0080~\u0001\u0000\u0000\u0000\u0080\u0081\u0001\u0000\u0000\u0000"+
		"\u0081\u0019\u0001\u0000\u0000\u0000\u0082\u0080\u0001\u0000\u0000\u0000"+
		"\u0083\u0084\u0005\u0019\u0000\u0000\u0084\u0085\u0003\u0014\n\u0000\u0085"+
		"\u0086\u0005\u001a\u0000\u0000\u0086\u008d\u0001\u0000\u0000\u0000\u0087"+
		"\u0088\u0005\u0011\u0000\u0000\u0088\u008d\u0003\u001a\r\u0000\u0089\u008a"+
		"\u0005\u0012\u0000\u0000\u008a\u008d\u0003\u001a\r\u0000\u008b\u008d\u0003"+
		"\u001c\u000e\u0000\u008c\u0083\u0001\u0000\u0000\u0000\u008c\u0087\u0001"+
		"\u0000\u0000\u0000\u008c\u0089\u0001\u0000\u0000\u0000\u008c\u008b\u0001"+
		"\u0000\u0000\u0000\u008d\u001b\u0001\u0000\u0000\u0000\u008e\u008f\u0007"+
		"\u0004\u0000\u0000\u008f\u001d\u0001\u0000\u0000\u0000\f),3@IWfiqx\u0080"+
		"\u008c";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}