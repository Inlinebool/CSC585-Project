package edu.stanford.nlp.kbp.slotfilling.common;

public class Props {
  public static final String ALTERNATE_DATE_HANDLING = "kbp.alternate.date.handling";
  public static final String ANALYSIS_KB = "analysis.kb";
  public static final String ANALYSIS_TEST_MODE = "analysis.test.mode";
  public static final String CORPUS_BASE_DIR = "corpus.base.dir";
  public static final String DEV_QUERIES = "devQueries";
  public static final String DOMAIN_SPEC_INFERENCE = "domain.inference";
  public static final String EPOCHS = "epochs";
  public static final String FEATURES = "features";
  public static final String FEATURE_COUNT_THRESHOLD = "featureCountThreshold";
  public static final String FILTER = "filter";
  public static final String FOLDS = "folds";
  public static final String INDEX = "index.kbp";
  public static final String MINIMAL_ANALYSIS = "index.minimal.analysis";
  public static final String OFFICIAL_INDEX = "index.official";
  public static final String INDEX_CACHE_DIR = "index.cache.dir";
  public static final String INDEX_PIPELINE_METHOD = "index.pipelinemethod";
  public static final String SENTENCE_CACHE = "index.sentencecache";
  public static final String TEST_SENTENCES_PER_ENTITY = "index.test.sentences.per.entity";
  public static final String TEST_WEBSENTENCES_PER_ENTITY = "index.test.websentences.per.entity";
  public static final String TEST_USEINDEXCACHE = "index.test.usecache";
  static public final String TEST_RESULT_SORT_MODE_PROPERTY = "index.test.sortmode";
  public static final String TRAIN_SENTENCES_PER_ENTITY = "index.train.sentences.per.entity";
  public static final String TRAIN_WEBSENTENCES_PER_ENTITY = "index.train.websentences.per.entity";
  public static final String TRAIN_USEINDEXCACHE = "index.train.usecache";
  static public final String TRAIN_RESULT_SORT_MODE_PROPERTY = "index.train.sortmode";
  public static final String TRAIN_USEKNOWNSLOTS = "index.train.useknownslots";
  public static final String INFERENCE_TYPE = "inference.type";
  public static final String JOINT_INCOMPLETE_NEGATIVES = "joint.incneg";
  public static final String KBP_COUNTRIES = "kbp.countries";
  public static final String INPUT = "kbp.datums.input";
  public static final String OUTPUT = "kbp.datums.output";
  public static final String IS_TEST = "kbp.datums.istest";
  public static final String KBP_DIAGNOSTICMODE = "kbp.diagnosticmode";
  public static final String ENTIRE_KB = "kbp.entire.kb";
  public static final String INPUT_KB = "kbp.inputkb"; // TODO: this is similar to ENTIRE_KB?
  public static final String GOLD_RESPONSES = "kbp.goldresponses";
  public static final String LIST_OUTPUT = "kbp.list.output";
  public static final String KBP_MANUAL_LISTS = "kbp.manual.lists";
  public static final String KBP_MAPPING = "kbp.mapping";
  public static final String NERENTRY_FILE = "kbp.ner.types";
  public static final String TEST_CACHE = "kbp.testcache";
  public static final String RUN_ID = "kbp.runid";
  public static final String KBP_STATES = "kbp.states";
  public static final String KBP_TEMPORAL = "kbp.temporal";
  public static final String KBP_TEMPORAL_SENTENCEEXTRACTOR = "kbp.temporal.sentenceExtractor";
  public static final String KB_SCORE_FILE = "kbScoreFile";
  public static final String LOG_LEVEL = "logLevel";
  public static final String MODEL_COMBINATION_ENABLED = "model.combination.enabled";
  public static final String MODEL_COMBINATION_INPUT_FILES = "model.combination.input";
  public static final String MODEL_COMBINATION_WEIGHT_BY_SCORES = "model.combination.weight.by.scores";
  public static final String MODEL_COMBINATION_NIL_WEIGHT = "model.combination.nil.weight";
  public static final String MODEL_COMBINATION_INPUTS_HAVE_SCORES = "model.combination.inputs.have.scores";
  public static final String MODEL_COMBINATION_SCORE_BIAS = "model.combination.score.bias";
  public static final String NATIONALITIES = "nationalities";
  public static final String NEGATIVES_SAMPLE_RATIO = "negatives.sampleratio";
  public static final String NLPSUB = "nlpsub";
  public static final String OVERLAPPING_RELATIONS = "overlapping.relations";
  public static final String PERCEPTRON_EPOCHS = "perceptron.epochs";
  public static final String PERCEPTRON_NORMALIZE = "perceptron.normalize";
  public static final String PERCEPTRON_SOFTMAX = "perceptron.softmax";
  public static final String PERCEPTRON_THRESHOLD = "perceptron.threshold";
  public static final String PRIORITY_FILE = "priority.file";
  public static final String QUERY_SCORE_FILE = "queryScoreFile";
  public static final String DOMAIN_ADAPT = "reader.domain.adapt";
  public static final String DOMAIN_ADAPT_STYLE = "reader.domain.adapt.style";
  public static final String ENFORCE_NE = "reader.enforcene";
  public static final String MULTI_MATCH = "reader.multimatch";
  public static final String NO_NEGATIVES = "reader.no.negatives";
  public static final String USE_WEB = "reader.useweb";
  public static final String READER_WEBCACHE = "reader.webcache";
  public static final String READER_LOG_LEVEL = "readerLogLevel";
  public static final String REGEX_IGNORE_CASE = "regexner.ignorecase";
  public static final String REGEX_MAP = "regexner.mapping";
  public static final String RELATION_FEATS = "relationFeatures";
  public static final String TRIGGER_WORDS = "relation.triggers";
  public static final String RULE_DIR = "rule.dir";
  public static final String SERIALIZED_MODEL_PATH = "serializedRelationExtractorPath";
  public static final String SLOT_THRESHOLD = "slot.threshold";
  public static final String SLOT_THRESHOLD_PER_RELATION = "slot.threshold.per.relation";
  public static final String STATES = "states";
  public static final String SCORE_TEST = "scoreTestQueries";
  public static final String SHOW_CURVE = "show.curve";
  public static final String TEMPORAL_BASELINE = "temporal.baseline";
  public static final String TEMPORAL_FILTER_DEP_PATHS = "temporal.filterpaths";
  public static final String TEMPORAL_GOV_VERB_FILTER = "temporal.govverbfilter";
  public static final String TEMPORAL_STARTWORDSFILE = "temporal.startwordsfile";
  public static final String TEMPORAL_ENDWORDSFILE = "temporal.endwordsfile";
  public static final String TEMPORAL_GOOGNGRAMSFILE = "temporal.googlengramsfile";
  public static final String TEMPORAL_LOGLEVEL = "temporal.logLevel";
  public static final String TEMPORAL_RESULTTRACE = "temporal.resulttrace";
  public static final String TEMPORAL_USESTARTEND = "temporal.useStartEnd";
  public static final String TEMPORAL_USEDOCDATE = "temporal.useDocDate";
  public static final String TEST_PATH = "testPath";
  public static final String TEST_QUERIES = "testQueries";
  public static final String TIME_COMBINATION = "temporal.timecombination";
  public static final String TRAINY = "trainy";
  public static final String DEFAULT_TIME_COMBINATION = "COMBINE";
  public static final String TRAINER = "trainer";
  public static final String MODEL_TYPE = "trainer.model";
  public static final String TRAIN_PATH = "trainPath";
  public static final String WORK_DIR = "work.dir";
  public static final String DOC_FINDING_DURING_TUNING = "doc.finding.during.tuning";
  public static final String INFERENCE_DURING_TUNING = "inference.during.tuning";
  public static final String MATCH_SLOTNE = "reader.matchSlotNE";
  public static final String ANYDOC = "score.anydoc";
}