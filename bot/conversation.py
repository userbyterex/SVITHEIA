from telegram import Update
from telegram.ext import ContextTypes

from core.agents.hypothesis import generate_hypothesis
from core.agents.experimenter import design_and_run_experiment
from core.agents.critic import attempt_falsification
from core.agents.knowledge import update_knowledge_graph


async def handle_scientific_question(update: Update, context: ContextTypes.DEFAULT_TYPE, question: str):
    """
    Runs the full Svitheia discovery loop and replies step by step.
    """
    chat_id = update.effective_chat.id

    # Step 1: Acknowledge
    await context.bot.send_message(
        chat_id=chat_id,
        text=f"Received question:\n_{question}_\n\nStarting discovery loop...",
        parse_mode="Markdown"
    )

    try:
        # Step 2: Generate hypothesis
        await context.bot.send_message(chat_id=chat_id, text="*Step 1 – Generating hypothesis...*", parse_mode="Markdown")
        hypothesis = await generate_hypothesis(question)
        await context.bot.send_message(
            chat_id=chat_id,
            text=f"*Hypothesis:*\n{hypothesis}",
            parse_mode="Markdown"
        )

        # Step 3: Design and run experiment
        await context.bot.send_message(chat_id=chat_id, text="*Step 2 – Designing and running experiment...*", parse_mode="Markdown")
        experiment_result = await design_and_run_experiment(question, hypothesis)
        await context.bot.send_message(
            chat_id=chat_id,
            text=f"*Experiment result:*\n{experiment_result}",
            parse_mode="Markdown"
        )

        # Step 4: Attempt falsification
        await context.bot.send_message(chat_id=chat_id, text="*Step 3 – Attempting falsification...*", parse_mode="Markdown")
        critique = await attempt_falsification(hypothesis, experiment_result)
        await context.bot.send_message(
            chat_id=chat_id,
            text=f"*Critic analysis:*\n{critique}",
            parse_mode="Markdown"
        )

        # Step 5: Update knowledge graph
        await context.bot.send_message(chat_id=chat_id, text="*Step 4 – Updating knowledge graph...*", parse_mode="Markdown")
        summary = await update_knowledge_graph(question, hypothesis, experiment_result, critique)
        await context.bot.send_message(
            chat_id=chat_id,
            text=f"*Final summary:*\n{summary}",
            parse_mode="Markdown"
        )

    except Exception as e:
        await context.bot.send_message(
            chat_id=chat_id,
            text=f"An error occurred during the discovery loop:\n`{str(e)}`",
            parse_mode="Markdown"
        )
