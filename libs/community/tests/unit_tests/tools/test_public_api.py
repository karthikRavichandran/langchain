"""Test the public API of the tools package."""
from langchain_community.tools import __all__ as public_api

_EXPECTED = [
    "AINAppOps",
    "AINOwnerOps",
    "AINRuleOps",
    "AINTransfer",
    "AINValueOps",
    "AIPluginTool",
    "APIOperation",
    "ArxivQueryRun",
    "AzureCogsFormRecognizerTool",
    "AzureCogsImageAnalysisTool",
    "AzureCogsSpeech2TextTool",
    "AzureCogsText2SpeechTool",
    "AzureCogsTextAnalyticsHealthTool",
    "BaseGraphQLTool",
    "BaseRequestsTool",
    "BaseSQLDatabaseTool",
    "BaseSparkSQLTool",
    "BaseTool",
    "BearlyInterpreterTool",
    "BingSearchResults",
    "BingSearchRun",
    "BraveSearch",
    "ClickTool",
    "CogniswitchKnowledgeSourceFile",
    "CogniswitchKnowledgeStatus",
    "CogniswitchKnowledgeSourceURL",
    "CogniswitchKnowledgeRequest",
    "ConneryAction",
    "CopyFileTool",
    "CurrentWebPageTool",
    "DeleteFileTool",
    "DuckDuckGoSearchResults",
    "DuckDuckGoSearchRun",
    "E2BDataAnalysisTool",
    "EdenAiExplicitImageTool",
    "EdenAiObjectDetectionTool",
    "EdenAiParsingIDTool",
    "EdenAiParsingInvoiceTool",
    "EdenAiSpeechToTextTool",
    "EdenAiTextModerationTool",
    "EdenAiTextToSpeechTool",
    "EdenaiTool",
    "ElevenLabsText2SpeechTool",
    "ExtractHyperlinksTool",
    "ExtractTextTool",
    "FileSearchTool",
    "GetElementsTool",
    "GmailCreateDraft",
    "GmailGetMessage",
    "GmailGetThread",
    "GmailSearch",
    "GmailSendMessage",
    "GoogleCloudTextToSpeechTool",
    "GooglePlacesTool",
    "GoogleSearchResults",
    "GoogleSearchRun",
    "GoogleSerperResults",
    "GoogleSerperRun",
    "HumanInputRun",
    "IFTTTWebhook",
    "InfoPowerBITool",
    "InfoSQLDatabaseTool",
    "InfoSparkSQLTool",
    "JiraAction",
    "JsonGetValueTool",
    "JsonListKeysTool",
    "ListDirectoryTool",
    "ListPowerBITool",
    "ListSQLDatabaseTool",
    "ListSparkSQLTool",
    "MerriamWebsterQueryRun",
    "MetaphorSearchResults",
    "MoveFileTool",
    "NasaAction",
    "NavigateBackTool",
    "NavigateTool",
    "O365CreateDraftMessage",
    "O365SearchEmails",
    "O365SearchEvents",
    "O365SendEvent",
    "O365SendMessage",
    "OpenAPISpec",
    "OpenWeatherMapQueryRun",
    "PubmedQueryRun",
    "PolygonFinancials",
    "PolygonLastQuote",
    "PolygonTickerNews",
    "RedditSearchRun",
    "QueryCheckerTool",
    "QueryPowerBITool",
    "QuerySQLCheckerTool",
    "QuerySQLDataBaseTool",
    "QuerySparkSQLTool",
    "ReadFileTool",
    "RequestsDeleteTool",
    "RequestsGetTool",
    "RequestsPatchTool",
    "RequestsPostTool",
    "RequestsPutTool",
    "SceneXplainTool",
    "SearchAPIResults",
    "SearchAPIRun",
    "SearxSearchResults",
    "SearxSearchRun",
    "ShellTool",
    "SlackGetChannel",
    "SlackGetMessage",
    "SlackScheduleMessage",
    "SlackSendMessage",
    "SleepTool",
    "StdInInquireTool",
    "StackExchangeTool",
    "SteamshipImageGenerationTool",
    "StructuredTool",
    "SteamWebAPIQueryRun",
    "Tool",
    "VectorStoreQATool",
    "VectorStoreQAWithSourcesTool",
    "WikipediaQueryRun",
    "WolframAlphaQueryRun",
    "WriteFileTool",
    "YahooFinanceNewsTool",
    "YouSearchTool",
    "YouTubeSearchTool",
    "ZapierNLAListActions",
    "ZapierNLARunAction",
    "authenticate",
    "format_tool_to_openai_function",
    "tool",
]


def test_public_api() -> None:
    """Test for regressions or changes in the public API."""
    # Check that the public API is as expected
    assert set(public_api) == set(_EXPECTED)
